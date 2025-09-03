from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from Patients.models import Patients,Tasks
from Patients.serializers import PatientSerializer,TaskSerializer


# View to create patient 
class PatientCreateAPIView(generics.ListCreateAPIView):
    queryset=Patients.objects.all()
    serializer_class=PatientSerializer

# View to update Delete Retrieve specific patient
class PatientRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset=Patients.objects.all()
    serializer_class=PatientSerializer
    lookup_field='id'


# creating tasks to specific patients
class TaskCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class=TaskSerializer

    def get_queryset(self):                         # gets the tasks of specific patient
        patient_id=self.kwargs['patient_id']
        return Tasks.objects.filter(patient_id=patient_id)
    
    def perform_create(self,serializer):            # saves the patient field of tasks model
        patient=get_object_or_404(Patients,id=self.kwargs['patient_id']) #check it once
        serializer.save(patient=patient)

    