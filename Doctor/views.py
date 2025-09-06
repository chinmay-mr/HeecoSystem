from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from Patients.models import Patients,Tasks
from Patients.serializers import PatientSerializer,TaskSerializer
from Users.permissions import IsDoctor
from Users.models import Doctor

# View to create patient 
class PatientCreateAPIView(generics.ListCreateAPIView):
    permission_classes=[IsDoctor]
    queryset=Patients.objects.all()
    serializer_class=PatientSerializer

# View to update Delete Retrieve specific patient
class PatientRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes=[IsDoctor]
    
    serializer_class=PatientSerializer
    lookup_field='id'

    def get_queryset(self):
        user=self.request.user

        try:
            doctor=Doctor.objects.get(doctor=user)
        except  Doctor.DoesNotExist:
            return Patients.objects.none()

        return Patients.objects.filter(doctor_assigned=doctor)
        
    


# creating tasks to specific patients
class TaskCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class=TaskSerializer

    def get_queryset(self):                         # gets the tasks of specific patient
        patient_id=self.kwargs['patient_id']
        return Tasks.objects.filter(patient_id=patient_id)
    
    def perform_create(self,serializer):            # saves the patient field of tasks model
        patient=get_object_or_404(Patients,id=self.kwargs['patient_id']) 
        serializer.save(patient=patient)



# Update Delete Retrive specific task of a patient
class TaskModifyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    lookup_field='id'

    def get_queryset(self):
        tasks_of_specific_patient=Tasks.objects.filter(patient=self.kwargs['patient_id'])
        return tasks_of_specific_patient






    