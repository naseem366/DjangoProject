from django.shortcuts import render
from .serializers import ProductSerializer
from ..models import Product
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly


class ProductModelViewSet(viewsets.ModelViewSet):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer
	#authentication_classes=[BasicAuthentication]
	#authentication_classes=[SessionAuthentication]
	#permission_classes=[IsAuthenticated]
	#permission_classes=[IsAuthenticatedOrReadOnly]
	#permission_classes=[AllowAny]
	#permission_classes=[IsAdminUser]

