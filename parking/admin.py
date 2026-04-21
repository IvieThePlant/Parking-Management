from django.contrib import admin
from .models import ParkingLot, ParkingSession

# Register your models here.
admin.site.register(ParkingLot)
admin.site.register(ParkingSession)