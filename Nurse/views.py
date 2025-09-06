from django.shortcuts import get_object_or_404
from Patients.models import Vitals,Patients,Tasks
from Patients.serializers import VitalSerializer,TaskSerializer
from rest_framework import generics
# Vitals view
# A nurse can check the vital in desired time and update, checking vitals could be task

#vital api view to note vitals
class VitalsAPIView(generics.ListCreateAPIView):
    serializer_class=VitalSerializer
    
    def get_queryset(self):
        patient_id=self.kwargs['patient_id']
        return Vitals.objects.filter(patient_id=patient_id)

    def perform_create(self,serializer):
        patient=get_object_or_404(Patients,id=self.kwargs['patient_id'])
        serializer.save(patient=patient)

#vitals api to retrieve and updtae specific vitals
class VitalsDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class=VitalSerializer
    lookup_field='id'
    
    def get_queryset(self):
        patient_id=self.kwargs['patient_id']
        return Vitals.objects.filter(patient_id=patient_id)
    
#API view to list all the tasks of a Nurse        
class TasksAPIView(generics.ListAPIView):
    serializer_class=TaskSerializer
    

    def get_queryset(self):
        queryset=Tasks.objects.filter(assigned_to_id=self.kwargs['Nurse_id'])
        return queryset
    
