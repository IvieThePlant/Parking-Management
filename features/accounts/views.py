from django.shortcuts import render

# Create your views here.
#Import default
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from parking.models import ParkingLot

#Override register function to redirect user to specific pages.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/accounts/login')
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


#Dashboard available only to logged in users
@login_required
def dashboard_view(request):
    lots = ParkingLot.objects.all()
    return render(request, 'accounts/dashboard.html', {'lots': lots})