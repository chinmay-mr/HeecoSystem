from django.shortcuts import render
from rest_framework import generics
from Patients.models import Patients
from Patients.serializers import PatientSerializer


# View to create patient 
class PatientCreateAPIView(generics.ListCreateAPIView):
    queryset=Patients.objects.all()
    serializer_class=PatientSerializer
    
class PatientRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset=Patients.objects.all()
    serializer_class=PatientSerializer
    lookup_field='pk'