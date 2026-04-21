from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class ParkingLot(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ParkingSession(models.Model):
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, related_name='parking_sessions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parking_sessions')
    occupied_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def end_session(self):
        if self.ended_at is not None: return None
        self.ended_at = timezone.now()
        self.save()
    
    @property
    def is_active(self) -> bool:
        return self.ended_at is None
    
    @property
    def duration(self) -> datetime.timedelta:
        if self.ended_at is None:
            return timezone.now() - self.occupied_at
        else:
            return self.ended_at - self.occupied_at
    
    def __str__(self) -> str:
        if self.ended_at is None:
            return f"{self.user.username} parked in lot {self.lot} at {self.occupied_at}"
        else:
            return f"{self.user.username} parked in lot {self.lot} from {self.occupied_at} to {self.ended_at}"
