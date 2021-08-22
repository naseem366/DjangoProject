from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework.authentication import BaseAuthentication
from rest_framework.status import (
                                        HTTP_200_OK,
                                    	HTTP_400_BAD_REQUEST,
                                    	HTTP_204_NO_CONTENT,
                                    	HTTP_201_CREATED,
                                    	HTTP_500_INTERNAL_SERVER_ERROR,
                                        HTTP_404_NOT_FOUND,
 
                                   ) 
from ..models import *

class UserCreateAPIView(APIView):
    def post(self,request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'account has been successfully'},status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            return Response({
                'message': 'Login successfully',
                'data': serializer.data
            }, status=200)
        error_keys = list(serializer.errors.keys())
        if error_keys:
            error_msg = serializer.errors[error_keys[0]]
            return Response({'message': error_msg[0]}, status=400)
        return Response(serializer.errors, status=400)


class GetUserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        user = request.user
        data = request.data
        try:
            obj = User.objects.all().filter(id=user.id)
            #obj = User.objects.get(id=user.id)
            
        except:
            return Response({
                'success' : 'False',
                'message' : 'No user found',
            },status=HTTP_400_BAD_REQUEST)
    
        serializer = GetUserProfileDetailsSerializer(obj,many=True)
        #serializer =GetUserProfileDetailsSerializer(data=data,context={'user':user})
        data       = serializer.data        
        return Response({
            'success' : 'True',
            'message' : 'Data retrieved successfully',
            'data'    : data
        },status=HTTP_200_OK)

class GetUserListAPIView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,*args,**kwargs):
        user=request.user
        qs = User.objects.all()
        serializer = GetUserProfileDetailsSerializer(qs,many=True)
        data       = serializer.data        
        return Response({
            'success' : 'True',
            'message' : 'Data retrieved successfully',
            'data'    : data
        },status=HTTP_200_OK)

import logging

class EditUserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        user       = request.user 
        data       = request.data
        files      = request.FILES

        logging.debug('User Edit Profile')
        logging.debug(data)
        logging.info('Login User')
        logging.info(user)

        serializer = EditUserProfileSerializer(data=data,files=files,context={'user':user})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success' : 'True',
                'message' : 'Profile updated successfully',
                },status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)            


'''
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'registered successfully'},status=HTTP_200_OK)
        error_keys = list(serializer.errors.keys())
        if error_keys:
            error_msg = serializer.errors[error_keys[0]]
            return Response({'message': error_msg[0]}, status=400)
        return Response(serializer.errors, status=400)
'''