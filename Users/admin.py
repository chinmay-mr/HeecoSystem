from django.contrib import admin
from . import models
from .models import Doctor
# Register your models here.
admin.site.register(Doctor)
admin.site.register(models.Nurse)
admin.site.register(models.Guardian)
