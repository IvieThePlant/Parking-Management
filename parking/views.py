from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ParkingLot
from django.conf import settings
#Create your views here

@login_required
def dashboard_view(request):
    lots = ParkingLot.objects.all()
    return render(request, 'parking/dashboard.html', {'lots': lots})


LOT_LOCATIONS = [
    {"coordinates": [-93.242878, 44.964812], "name": "Lot A", "spotsTaken": 10, "totalSpots": 30},
    {"coordinates": [-93.241709, 44.964796], "name": "Lot B", "spotsTaken": 8,  "totalSpots": 20},
    {"coordinates": [-93.243197, 44.965065], "name": "Lot D", "spotsTaken": 23, "totalSpots": 30},
    {"coordinates": [-93.242081, 44.965318], "name": "Lot E", "spotsTaken": 5,  "totalSpots": 20},
    {"coordinates": [-93.242024, 44.967266], "name": "Lot G", "spotsTaken": 18, "totalSpots": 30},
    {"coordinates": [-93.239643, 44.966379], "name": "Lot J", "spotsTaken": 20, "totalSpots": 30},
    {"coordinates": [-93.238787, 44.966341], "name": "Lot K", "spotsTaken": 12, "totalSpots": 20},
    {"coordinates": [-93.237113, 44.965077], "name": "Lot L", "spotsTaken": 15, "totalSpots": 60},
]

@login_required
def map_view(request):
    return render(request, "parking/map.html", {
        "locations": LOT_LOCATIONS
    })