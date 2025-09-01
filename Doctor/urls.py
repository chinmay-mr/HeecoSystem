from django.contrib import admin
from django.urls import path
from .views import PatientCreateAPIView
urlpatterns = [
    path('patients/',PatientCreateAPIView.as_view(),name='create-patients'),


]