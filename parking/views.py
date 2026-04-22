from django.contrib import messages
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
    session = ParkingSession.objects.get(ParkingSession, id=session_id, user=request.user)

    session.end_session()

    return redirect('dashboard')