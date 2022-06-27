from django.shortcuts import render

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response 
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    def post(self,request,format=None):
        serializer = RegisterSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('the user is created')
class LoginView(APIView):
    def post(self,request,format=None):
        serializer = LoginSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True) 
        username = serializer.data.get('username')    
        password = serializer.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            tokens = get_tokens_for_user(user)
            return Response({'tokens':tokens,'msg':'the user is sucessfully logged in'},status=status.HTTP_200_OK)

        else:
            return Response('the username or password is incorrect')    


class ChangePasswordView(APIView):
    def post(self,request,format=None):
        permission_classes = [IsAuthenticated]
        serializer = ChangePasswordSerializer(data=request.data,context={'user':self.request.user})
        if serializer.is_valid():
            current_password = serializer.data.get('current_password')
            user = self.request.user
            checking = user.check_password(current_password)
            if checking:
                user.set_password(current_password)
                user.save()
                return Response('the password is changed sucessfully')
            
        
            else:
                return Response('the current password is not correct')


        else:
            return Response(serializer.errors)    
    
       
    
                

       

        
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.user
        print(user)
        tokens = get_tokens_for_user(user)
        return Response({'tokens':tokens,'msg':'the registration through facebook is sucessfull'})
        # check what you get in response from parent class post method.
        

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/Acoounts/github/login/callback/"
    client_class = OAuth2Client