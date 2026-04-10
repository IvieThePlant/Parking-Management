from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ParkingLot

#Create your views here

@login_required
def dashboard_view(request):
    lots = ParkingLot.objects.all()
    return render(request, 'parking/dashboard.html', {'lots': lots})