from Acoounts.views import FacebookLogin, GithubLogin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *


urlpatterns = [
    
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(),name='resgiter'),
    path('login/',LoginView.as_view(),name='login'),
    path('changepassword/',ChangePasswordView.as_view(),name='changepassword')

]
