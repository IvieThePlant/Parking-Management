from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ParkingLot, ParkingSpot, ParkingSession
from .service import ParkingSessionToJSON

# Create your views here.
# Useful Documentation: https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme

# Create Session using POST
# URL - {domainName}/api/sessions/create/
# BODY - {"spot_id" : ?, "end_time": ?}
# RESPONSE (JSON) - {(session object)}

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSession(request):
    user = request.user
    spot_id = request.data.get('spot_id')
    end_time = request.data.get('end_time')

    #Check to see if request includes spot_id in body (Tested Using PostMan)
    if not spot_id:
        return Response({"ERROR": "spot_id & end_time is needed in body"}, status=400)

    try:
        spot = ParkingSpot.objects.get(id=spot_id)

        # Check to see if spot is available
        if not spot.is_available:
            return Response({"ERROR": "Spot is not available"}, status=400)

        # Create Session
        session = ParkingSession.objects.create(user=user, spot=spot)

        # Update spot to occupied so to prevent double booking
        spot.is_available = False
        spot.save()
        # Return sessions as JSON
        return Response(ParkingSessionToJSON(session).data, status=201)

    except ParkingSpot.DoesNotExist:
        # Return sessions as JSON
        return Response({"ERROR": "Spot not found"}, status=404)