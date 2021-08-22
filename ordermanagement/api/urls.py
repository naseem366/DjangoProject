from django.contrib import admin
from django.urls import path
from  ordermanagement.api import views

urlpatterns = [
    
    path('orderapi/', views.OrderList.as_view()),
    #path('categoryapi/<int:pk>',views.CategoryRetrieveUpdateDestroy.as_view()),

]
