from django.db import models

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
    pass
