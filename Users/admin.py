from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Nurse)
admin.site.register(models.Guardian)
