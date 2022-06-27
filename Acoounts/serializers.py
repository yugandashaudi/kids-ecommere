from unittest.util import _MAX_LENGTH
from colorama import Style
from rest_framework import serializers
from django.contrib.auth.models import User 

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User 
        fields=['username','email','password','confirm_password']


    def validate(self,attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('The password and confrim_password doesnot match')

        return attrs

    def create(self,validate_data):
        validate_data.pop('confirm_password')

        user = User.objects.create(username= validate_data['username'],email=validate_data['email'])     
        user.set_password(validate_data['password'])  
        user.save() 
        return user 

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    class Meta:
        model =User 
        fields=['username','password']
   
class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100,write_only = True)   
    confirm_password = serializers.CharField(max_length=100,write_only = True)
    class Meta:
        fields = ['current_password','new_password','confirm_password']

    def validate(self,attrs):
       
      
        if attrs['new_password']  != attrs['confirm_password']:
            return serializers.ValidationError('The new password and confirm password doesnot matched')  

       
    
        return attrs   



   
            
