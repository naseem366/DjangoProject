
from rest_framework.response import Response
from .serializers import OrderSerializer
from ..models import OrderPlaced
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,CreateAPIView,
RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,
RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)

# Create your views here.
class OrderList(ListAPIView):
	queryset=OrderPlaced.objects.all()
	serializer_class=OrderSerializer


	
