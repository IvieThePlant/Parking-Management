from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ParkingLot, ParkingSession


#Create your views here

@login_required
def dashboard_view(request):
    lots = ParkingLot.objects.all()
    return render(request, 'parking/dashboard.html', {'lots': lots})

@login_required
def create_session(request):

    #If API Method call is POST
    if request.method == 'POST':
        lot = request.POST.get("lot")
        license = request.POST.get("license")

        #GET parking lot from ParkingLots table
        lot = ParkingLot.objects.get(id=lot)

        # Create Session with information from form
        ParkingSession.objects.create(user=request.user, lot=lot, license=license)

        #Upon Successful insert redirect to mySession page (LANDING PAGE FOR NOW UNTIL MYSESSIONS HTML IS COMPLETE)
        return redirect('landing')

    return render(request, 'landing.html')