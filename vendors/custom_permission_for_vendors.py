from rest_framework.permissions import BasePermission
from rest_framework import permissions


class VendorPermission(BasePermission):
    edit_methods = ("PUT", "PATCH","POST","GET")
    def has_permission(self, request, view):
        if request.method == ("GET"):
            if  request.user.is_authenticated:
                return True
            return False    

        if request.method == ("POST","PUT","PATCH"):
            if request.user.groups.filter(name='vendor').first(): 
                return True  
            return False    
        
        return False    

    
    