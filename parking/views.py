from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ParkingLot
from .models import ParkingSession
from django.conf import settings
from django.db.models import Count
#Create your views here

@login_required
def dashboard_view(request):
    lots = ParkingLot.objects.all()
    return render(request, 'parking/dashboard.html', {'lots': lots})


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