from django.urls import path
from .views import VitalsAPIView,VitalsDetailAPIView,TasksAPIView

urlpatterns = [
    path('patients/<int:patient_id>/vitals/',VitalsAPIView.as_view(),name='Vitals-ListCreate'),
    path('patients/<int:patient_id>/vitals/<int:id>',VitalsDetailAPIView.as_view(),name='vitals-detial'),
    path('<int:Nurse_id>/tasks/',TasksAPIView.as_view(),name='list-tasks of nurse'),
    # path('tasks/'),

]   