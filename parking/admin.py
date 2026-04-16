from django.contrib import admin
from .models import ParkingLot, ParkingSpot, ParkingSession

# Register your models here.
admin.site.register(ParkingLot)
admin.site.register(ParkingSpot)
admin.site.register(ParkingSession)