from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import Doctor

class IsDoctor(BasePermission):
    
    def has_permission(self,request,view):
        user=request.user

        if not user.is_authenticated:
            return False

        return Doctor.objects.filter(doctor=user).exists()

        def has_object_permission(self,request,view,obj):
            return self.has_permission(request,view)