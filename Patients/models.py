from django.db import models
from Users.models import Guardian,Doctor,Nurse
# Create your models here.
class Patients(models.Model):
    name=models.CharField()
    condition=models.CharField()
    condition_description=models.TextField()
    process=models.TextField(null=True,blank=True)
    admission_date=models.DateTimeField(auto_now_add=True)
    discharge_date=models.DateTimeField(blank=True,null=True)

    guardian=models.OneToOneField(Guardian,on_delete=models.DO_NOTHING,null=True,related_name="patient")
    doctor_assigned=models.OneToOneField(Doctor,on_delete=models.DO_NOTHING,null=True,related_name="patient") #change it doctor assigning

    def __str__(self):
        return self.name


class GeneralDetail(models.Model):
    patient=models.OneToOneField(Patients,on_delete=models.CASCADE,related_name='general_details')
    blood_group=models.CharField()
    age=models.PositiveIntegerField()
    medical_history=models.TextField()

    floor_no=models.CharField()
    bed_no=models.CharField()

    def __str__(self):
        return f"{self.patient.name} - floor {floor_no} bed {bed_no}"

class Vitals(models.Model):
    patient=models.OneToOneField(Patients,on_delete=models.CASCADE,related_name="vitals")
    temperature=models.FloatField()
    heart_rate=models.IntegerField()
    respiratory_rate=models.IntegerField()
    oxygen_saturation=models.IntegerField()
    check_time=models.DateTimeField()
    checked_by=models.OneToOneField(Nurse,on_delete=models.DO_NOTHING,related_name='patient_vitals')
    remarks=models.TextField()

    def __str__(self):
        return self.patient.name

class Tasks(models.Model):
    class Status(models.TextChoices):
        PENDING='pending'
        COMPLETED='completed'
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name="tasks")
    task_type=models.TextField()
    task=models.TextField()
    assigned_to=models.ForeignKey(Nurse,null=True,on_delete=models.DO_NOTHING,related_name="tasks")
    status=models.CharField(choices=Status.choices,default=Status.PENDING)
    assigned_time=models.DateField(auto_now_add=True)
    due_time=models.DateField()
    completed_time=models.DateField(null=True,blank=True)

    def save(self,*args,**kwargs):

        if self.status=='completed' and self.comleted_time is None:
            self.comleted_time=timezone.now()

        if self.status=='pending':
            self.comleted_time=None
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{patient.name} due:{due_time} status:{status}"
    
    

    

    


    

