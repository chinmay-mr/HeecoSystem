from rest_framework import serializers
from .models import Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=['id','name','condition','condition_description','admission_date','discharge_date','guardian','doctor_assigned']
        read_only_fields = ['id','admission_date']
