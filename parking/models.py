from django.db import models
from django.db import models
from django.contrib.auth.models import User

class ParkingLot(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ParkingSpot(models.Model):
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, related_name='spots')
    spot_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField()

    def __str__(self):
        return f"{self.lot.name} - Spot {self.spot_number}"

class ParkingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey('ParkingLot', on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - Lot {self.lot.name} - started_at {self.started_at} - ended_at {self.ended_at} - available {self.available}"
