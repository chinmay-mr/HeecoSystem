from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    doctor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctor")
    license_number=models.CharField(unique=True)
    specialization=models.CharField()
    years_of_experience=models.PositiveIntegerField()
    # patients

    def __str__(self):
        return f"{self.doctor.id}"
        
    


class Nurse(models.Model):
    class Shift(models.TextChoices):
        DAY_SHIFT='dayshift','Dayshift'
        NIGHT_SHIFT='nightshift','Nightshift'
        
    
    nurse=models.ForeignKey(User,on_delete=models.CASCADE,related_name="nurse",default="")
    shift=models.CharField(choices=Shift.choices,default=Shift.DAY_SHIFT)
    # patients

    def __str__(self):
        return f"{self.nurse}"

class Guardian(models.Model):
    name=models.CharField(null=True,blank=True)
    phone_number=models.CharField(unique=True,null=True,blank=True,default="Not Filled")
    relation_type=models.CharField()

    # patient
    
    def __str__(self):
        return f"{name} {relation_type}"
