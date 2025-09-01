from django.shortcuts import render
from rest_framework import generics
from Patients.models import Patients
from Patients.serializers import PatientSerializer


# View to create patient 
class PatientCreateAPIView(generics.CreateAPIView):
    queryset=Patients.objects.all()
    serializer_class=PatientSerializer
    