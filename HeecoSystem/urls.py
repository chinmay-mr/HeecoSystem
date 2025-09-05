from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctor/',include("Doctor.urls"),name="Doctor-ops"),
    path('api/Nurse/',include("Nurse.urls"),name="Nurse-ops"),

]
