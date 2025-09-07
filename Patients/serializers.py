from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Patients,Tasks,Vitals
from Users.models import Guardian,Doctor,Nurse
from Users.serializers import GuardianSerializer,NurseSerializer



class PatientSerializer(serializers.ModelSerializer):

    guardian=GuardianSerializer()

    class Meta:
        model=Patients
        fields=['id','name','condition','condition_description','admission_date','discharge_date','guardian','doctor_assigned']
        read_only_fields = ['id','admission_date','doctor_assigned']
    
    def create(self, validated_data):
        request = self.context['request']
        doctor = Doctor.objects.get(doctor=request.user)
    
        guardian_data = validated_data.pop('guardian')
        guardian, created = Guardian.objects.get_or_create(**guardian_data)
        patient = Patients.objects.create(guardian=guardian,doctor_assigned=doctor ,**validated_data)
        return patient

    def update(self, instance, validated_data):
    # Pop nested guardian data if provided
        guardian_data = validated_data.pop('guardian', None)

        # Update top-level patient fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Only try to update guardian if guardian data was provided
        if guardian_data is not None:
            # Try to get the current guardian
            guardian = getattr(instance, 'guardian', None)

            if guardian:
                # Update existing guardian
                for attr, value in guardian_data.items():
                    setattr(guardian, attr, value)
                guardian.save()
            else:
                # Create new guardian and assign to patient
                guardian = Guardian.objects.create(**guardian_data)
                instance.guardian = guardian
                instance.save()

        return instance


class AbstractPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=['id','name','condition','guardian','doctor_assigned']

class TaskSerializer(serializers.ModelSerializer):
    
    patient=AbstractPatientSerializer(read_only=True)
    
    class Meta:
        model=Tasks
        fields=['id','patient','task_type','task','assigned_to','status','due_time','completed_time']
        read_only_fields=['patient']
        


class VitalSerializer(serializers.ModelSerializer):
    patient=AbstractPatientSerializer(read_only=True)
    # checked_by=NurseSerializer() # need to verify with user
    class Meta:
        model=Vitals
        fields=['id','patient','temperature','heart_rate','respiratory_rate','oxygen_saturation','remarks','check_time','checked_by']
        read_only_fields=['check_time']