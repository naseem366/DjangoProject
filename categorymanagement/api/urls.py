from django.contrib import admin
from django.urls import path
from categorymanagement.api import views

urlpatterns = [
    
    path('categoryapi/', views.CategoryListCreate.as_view()),
    path('categoryapi/<int:pk>',views.CategoryRetrieveUpdateDestroy.as_view()),

]
