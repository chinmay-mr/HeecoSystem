from django.contrib import admin
from django.urls import path
from .views import PatientCreateAPIView,PatientRetrieveUpdateView,TaskCreateAPIView,TaskModifyAPIView
urlpatterns = [
    path('patients/',PatientCreateAPIView.as_view(),name='ListCreate-patients'),
    path('patients/<int:id>/',PatientRetrieveUpdateView.as_view(),name='retrieveUpdate-patients'),
    path('patients/<int:patient_id>/tasks/',TaskCreateAPIView.as_view(),name='create-list-tasks'),
    path('patients/<int:patient_id>/tasks/<int:id>',TaskModifyAPIView.as_view(),name='modify-tasks'),


]