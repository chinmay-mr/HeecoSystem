from django.contrib import admin
from django.urls import path
from .views import PatientCreateAPIView,PatientRetrieveUpdateView
urlpatterns = [
    path('patients/',PatientCreateAPIView.as_view(),name='ListCreate-patients'),
    path('patients/<int:pk>/',PatientRetrieveUpdateView.as_view(),name='retrieveUpdate-patients'),


]