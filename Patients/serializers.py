from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Patients,Tasks
from Users.models import Guardian
from Users.serializers import GuardianSerializer



class PatientSerializer(serializers.ModelSerializer):

    guardian=GuardianSerializer()

    class Meta:
        model=Patients
        fields=['id','name','condition','condition_description','admission_date','discharge_date','guardian','doctor_assigned']
        read_only_fields = ['id','admission_date']
    
    def create(self, validated_data):
        guardian_data = validated_data.pop('guardian')
        guardian, created = Guardian.objects.get_or_create(**guardian_data)
        patient = Patients.objects.create(guardian=guardian, **validated_data)
        return patient


class TaskSerializer(serializers.ModelSerializer):
    
    patient=PatientSerializer(read_only=True)
    
    class Meta:
        model=Tasks
        fields=['id','patient','task_type','task','assigned_to','status','due_time','completed_time']
        read_only_fields=['patient']


    