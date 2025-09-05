from rest_framework import serializers
from .models import Guardian,Nurse

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guardian
        fields='__all__'

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nurse
        fields=['id','name','shift']