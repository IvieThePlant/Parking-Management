from rest_framework import serializers
from .models import ParkingSession

#Converts Python Object to JSON Object
class ParkingSessionToJSON(serializers.ModelSerializer):
    class Meta:
        model = ParkingSession
        fields = '__all__'
