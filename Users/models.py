from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    doctor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctor")
    license_number=models.CharField(unique=True)
    specialization=models.CharField()
    years_of_experience=models.PositiveIntegerField()
    # patients

    def __str__(self):
        return f"{doctor.first_name}"
        
    


class Nurse(models.Model):
    class Shift(models.TextChoices):
        DAY_SHIFT='dayshift','Dayshift'
        NIGHT_SHIFT='nightshift','Nightshift'
        

    nurse=models.ForeignKey(User,on_delete=models.CASCADE,related_name="nurse")
    shift=models.CharField(choices=Shift.choices,default=Shift.DAY_SHIFT)
    # patients

    def __str__(self):
        return f"{nurse.first_name}"

class Guardian(models.Model):
    guardian=models.ForeignKey(User,on_delete=models.CASCADE,related_name="guardian")
    relation_type=models.CharField()

    # patient
    
    def __str__(self):
        return f"{guardian.first_name}"
