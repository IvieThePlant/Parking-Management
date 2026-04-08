from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ParkingLot, ParkingSpot, ParkingSession

# Create your views here.
# Useful Documentation: https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme

# Create Session using POST
# URL - {domainName}/api/sessions/create/
# BODY - {"spot_number" : ?, "lot_name": ?}
# RESPONSE (JSON) - {{result}}

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_session(request):
    user=request.user
    spot_number = request.data.get('spot_number')
    lot = request.data.get('lot_name')

    #Check to see if request includes spot_number, end_time and lot_name in body (Tested Using PostMan)
    if not spot_number or not lot:
        return Response({"ERROR": "spot_number & lot_name is needed in body"}, status=400)

    try:
        #GET BY SPOT_NUMBER AND LOT_NAME INSTEAD OF ID( __ )
        spot = ParkingSpot.objects.get(spot_number=spot_number, lot__name=lot)

        # Check to see if spot is available
        if not spot.available:
            return Response({"ERROR": "Spot is not available"}, status=400)

        # Create Session
        #(TESTING USER) temp_user = User.objects.get(username="Temp")
        session = ParkingSession.objects.create(user=user, spot=spot)

        # Update spot to occupied so to prevent double booking
        spot.available = False
        spot.save()

        result = []
        result.append({
            'user_id': session.user.id,
            'session_id': session.id,
            'spot_number': session.spot.spot_number,
            'lot_name': session.spot.lot.name,
            'start_time': session.start_time,
            'end_time': session.end_time,
            'status': session.status
        })
        # Return sessions as JSON
        return Response(result, status=201)

    except ParkingSpot.DoesNotExist:
        # Return sessions as JSON
        return Response({"ERROR": "Spot not found"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_generic_lot_info(request):
    """
    Summary:
    Gets all lot info

    Parameters:
    arg1 (request): Http request

    Returns:
    Response: JSON obj and status (200, 400, 404, etc)

    """

    if not lot:
        return Response({"ERROR": "No lots available"}, status = 400)

    # Runs multiple queries
    lots = ParkingLot.objects.all()

    result = []
    for lot in lots:
        result.append({
            'lot_id': lot.id,
            'lot_name': lot.name,
            'total_spots': lot.spots.count()
        })

    return Response(result, status = 200)

