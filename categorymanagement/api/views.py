
from rest_framework.response import Response
from .serializers import CategorySerializer
from ..models import Category
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,CreateAPIView,
RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,
RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BaseAuthentication, BasicAuthentication

# Create your views here.
class CategoryListCreate(ListCreateAPIView):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer
authentication_classes=[BasicAuthentication]
permission_classes=[IsAuthenticatedOrReadOnly]
    

class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer

	
