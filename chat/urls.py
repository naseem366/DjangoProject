from django.urls import path

from . import views

urlpatterns = [
    path('', views.index1, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

