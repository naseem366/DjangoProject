from logging import error
from django.db.models import fields
from rest_framework.permissions import AllowAny
from rest_framework.serializers import *
from rest_framework import serializers
from rest_framework.serializers import Serializer,ModelSerializer
from ..models import *
from rest_framework.serializers import EmailField
from rest_framework.fields import EmailField
import re
from django.core.mail import send_mail
from rest_framework.exceptions import APIException

class APIException400(APIException):
    status_code = 400


def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
        return False

class UserCreateSerializer(Serializer):
    full_name = CharField(error_messages={'required':'Full name is required', 'blank':'Full name is required'},max_length=400)
    email = EmailField(error_messages={'required':'Eamil is required', 'blank':'Email is required'},max_length=400)
    password=CharField(error_messages={'required':'Password is required', 'blank':'Password is required'})
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        if check_email(email) and User.objects.filter(email=email).exists():
            raise ValidationError('Email is not valid.Please enter valid Email')
        print(password)
        print(email)    
        if password.isalpha() == True:
            raise ValidationError('Password must be alpha numeric')
        return data
    def create(self, validated_data):
        full_name = self.validated_data['full_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        user=User.objects.create_user(email=email,password=password)
        user.full_name=full_name
        user.set_password(password)
        user.save()
        return validated_data

class UserLoginSerializer(Serializer):
    email = EmailField(error_messages={'required':'email key is required','blank':'email is required'})
    password = CharField(write_only=True,required=True,error_messages={'required': 'password key is required', 'blank': 'Password is required'})
    class Meta:
        model=User

class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile
        fields=('city','phone_number','profile_image')

class GetUserProfileDetailsSerializer(ModelSerializer):

    profile=ProfileSerializer()

    class Meta:
        model  = User
        fields=('full_name','email','profile','is_active')
        
        
class EditUserProfileSerializer(ModelSerializer):
    full_name   = serializers.CharField(error_messages={"required":"full_name key is required"},allow_blank=True)
    email    = serializers.CharField(error_messages={"required":"email key is required"},allow_blank=True)
    phone_number      = serializers.CharField(error_messages={"required":"phone number key is required"},allow_blank=True)
    city         = serializers.CharField(error_messages={"required":"city key is required"},allow_blank=True)
    profile_image = serializers.ImageField(required=False,allow_empty_file =True,allow_null=True)

    class Meta:
        model  = Profile
        fields = ['city','phone_number','profile_image','full_name','email']

    def validate(self,data):
        full_name   = data['full_name']
        email    = data['email']
        phone_number      = data['phone_number']
        city         = data['city']
        #state       = data['state']
        #zipcode      = data['zipcode']
        #address       =data['address']
        #profileimg   = data['profileimg']
        
        if not full_name or full_name =='':
            raise APIException400({
        'success' : 'False',
        'message' : 'first name is required'
        })    

        if not email or email == '':
            raise APIException400({
        'success' : 'False',
        'message' : 'last name is required'
        })

       
        if not city or city == '':
            raise APIException400({
        'success' : 'False',
        'message' : 'city is required'
        })
        

        if not phone_number or phone_number =='':
            raise APIException400({
                'success':'False',
                'message':'phone number is required'
        })
    

        # if profileimg is None:
        #     raise APIException400({
        # 'success' : 'False',
        # 'message' : 'please provide profile image'
        # })

        return data 

    def create(self,validated_data):
        full_name   = validated_data['full_name']
        email    = validated_data['email']
        phone_number      = validated_data['phone_number']
        city         = validated_data['city']
        #zipcode      = validated_data['zipcode']
        #state      = validated_data['state']
        #address    =validated_data['address']
        profile_image   = validated_data.get('profile_image')
        
        user      = self.context.get('user')
        otherUser = Profile.objects.filter(user=user).first()
        if not otherUser:
            raise APIException({
        'success' : 'False',
        'message' : 'This user is not registerd'
        })

        user.full_name        = full_name
        user.email         = email
        user.save() 

        otherUser.phone_number      = phone_number
        otherUser.city         = city
        #otherUser.zipcode      = zipcode
        #otherUser.state       = state
        #otherUser.address     =address
        
        
        if profile_image:
            print('image')
            print('profileimg',profile_image)
            otherUser.profileimg   = profile_image
        else:
            print('profileimg',profile_image)
            print('nope')

        otherUser.save()

        return validated_data

'''''
class UserCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['full_name','email','password']
'''''
