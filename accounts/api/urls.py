from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
   
urlpatterns = [
    path('registerapi/',views.UserCreateAPIView.as_view()),
    path('loginapi/',views.UserLoginAPIView.as_view()),
    path('getuserapi/',views.GetUserProfileAPIView.as_view()),
    path('getuserlistapi/',views.GetUserListAPIView.as_view()),
    path('edituserapi/',views.EditUserProfileAPIView.as_view()),
   

]
