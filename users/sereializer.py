from rest_framework import serializers
from .models import Usersdata,Teamreg,AboutEvents
class UsersdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usersdata
        fields="__all__"
class TeamregSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teamreg
        fields="__all__"
class AboutEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutEvents
        fields="__all__"
    