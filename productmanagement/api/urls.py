from django.contrib import admin
from django.urls import path,include
from productmanagement.api import views
from rest_framework.routers import DefaultRouter

#creating Router objects
router=DefaultRouter()

#register studentviewset wiht router
router.register('productapi',views.ProductModelViewSet,basename='student'),

urlpatterns = [

    path('',include(router.urls)),
]
