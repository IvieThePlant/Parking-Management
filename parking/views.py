from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ParkingLot
from .models import ParkingSession
from django.conf import settings
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#Create your views here

@login_required
def dashboard_view(request):
    lots = ParkingLot.objects.all()
    return render(request, 'parking/dashboard.html', {'lots': lots})

@login_required
def my_sessions(request):
    sessions = ParkingSession.objects.filter(user=request.user)

    lots = ParkingLot.objects.all()
    active_sessions = sessions.filter(ended_at__isnull=True).order_by('occupied_at')
    previous_sessions = sessions.filter(ended_at__isnull=False).order_by('ended_at')

    return render(request, 'parking/mysessions.html', {
        'active_sessions': active_sessions,
        'previous_sessions': previous_sessions,
        'lots': lots
    })


LOT_LOCATIONS = [
    {"coordinates": [-93.242878, 44.964812], "name": "Lot A", "totalSpots": 30},
    {"coordinates": [-93.241709, 44.964796], "name": "Lot B", "totalSpots": 20},
    {"coordinates": [-93.243197, 44.965065], "name": "Lot D", "totalSpots": 30},
    {"coordinates": [-93.242081, 44.965318], "name": "Lot E", "totalSpots": 20},
    {"coordinates": [-93.242024, 44.967266], "name": "Lot G", "totalSpots": 30},
    {"coordinates": [-93.239643, 44.966379], "name": "Lot J", "totalSpots": 30},
    {"coordinates": [-93.238787, 44.966341], "name": "Lot K", "totalSpots": 20},
    {"coordinates": [-93.237113, 44.965077], "name": "Lot L", "totalSpots": 60},
]

"""
Function combines LOT_LOCATION meta data and combines with current parking sessions

spotsTaken is calculated through filtering current count of parking sessions in each lot
"""
@login_required
def map_view(request):
    # NOTICE: this variable 'count' was made using generative AI (Opus)
    # Previous: For each loop 
    # Current: Query one liner
    counts = dict(
        ParkingSession.objects
        .filter(ended_at__isnull=True)
        .values_list("lot__name")
        .annotate(n=Count("id"))
    )
    locations = [
        {
            "name": loc["name"],
            "coordinates": loc["coordinates"],
            "totalSpots": loc["totalSpots"],
            "spotsTaken": counts.get(loc["name"], 0),
        }
        for loc in LOT_LOCATIONS
    ]
    
    """
    if list comprehension is buggy, resort to the following for each loop

    locations = []
    for loc in LOT_LOCATIONS:
        locations.append({
            "name": loc["name"],
            "coordinates": loc["coordinates"],
            "totalSpots": loc["totalSpots"],
            "spotsTaken": counts.get(loc["name"], 0),
        })
    """
    return render(request, "parking/map.html", {
        "locations": locations
    })

@login_required
def create_session(request):

    #If API Method call is POST
    if request.method == 'POST':
        lot = request.POST.get("lot")

        #GET parking lot from ParkingLots table
        lot = ParkingLot.objects.get(id=lot)

        #USER ONLY HAS 1 ACTIVE SESSION
        active_session = ParkingSession.objects.filter(user=request.user, ended_at=None).first()
        if active_session:
            messages.error(request, "You already have an active parking session.");
            return redirect('dashboard')

        # Create Session with information from form
        ParkingSession.objects.create(user=request.user, lot=lot)
        messages.success(request, "Parking session created successfully.")

        #Upon Successful insert redirect to mySession page (LANDING PAGE FOR NOW UNTIL MYSESSIONS HTML IS COMPLETE)
        return redirect('dashboard')

    return render(request, 'dashboard.html')

@login_required
def end_session(request, session_id):
    try:
        session = ParkingSession.objects.get(
            id=session_id,
            user=request.user
        )
    except ParkingSession.DoesNotExist:
        messages.error(request, "Parking session does not exist.");
        return redirect('mysessions')

    session.end_session()
    return redirect('mysessions')