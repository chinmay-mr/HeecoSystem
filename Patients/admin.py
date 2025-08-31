from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Patients)
admin.site.register(models.GeneralDetail)
admin.site.register(models.Vitals)
admin.site.register(models.Tasks)

