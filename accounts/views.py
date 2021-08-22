from collections import namedtuple
#from django.db.models.query_utils import Q
from django.db.models import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from pyrebase.pyrebase import Firebase
from .forms import CustomerRegistrationForm
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User

from rest_framework.response import Response
from django.http import HttpResponse
import json
import random
from datetime import datetime, timedelta
from django.views import View
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from  django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def UserManagement(request):
    #if request.user.is_superuser==True:
        #form=User.objects.all()
        #return render(request,'admin_panel/user-management.html',{'form':form})
    #else:
    #    return render(request,'admin_panel/permission.html')
        
    if request.method == "POST":
        fromdate=request.POST['fromdate']
        todate=request.POST['todate']

        searchresult=User.objects.filter(Q(date_joined__gte=fromdate) & Q(date_joined__lte=todate))

        #context={'searchresult':searchresult,'fromdate':fromdate,'todate':todate}

        #searchresult=User.objects.raw('select id,full_name,date_joined from user where date_joined between "'+fromdate+'" and "'+todate+'" ')

        return render(request,'admin_panel/user-management.html',{'data':searchresult})
    else:
        displaydata=User.objects.all()
        return render(request,'admin_panel/user-management.html',{'data':displaydata})

    

def check_blank_or_null(data):
	status=True
	for x in data:
		if x=="" or x==None:
			status=False
			break
		else:
			pass					
	return status

class send_otp(View):
    
    def post(self,request):
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            if forgetotp.objects.filter(user=user).exists():
                fotp=forgetotp.objects.get(user=user)
                fotp.delete()
            otp=random.randint(1000,10000)    
            fotp=forgetotp.objects.create(user=user)
            fotp.code=otp
            fotp.expire=datetime.now()+timedelta(minutes=10)
            fotp.save()
            send_mail("otp", f"Your password reset otp {otp}.Please do not share to anyone." ,settings.EMAIL_HOST_USER,[email,] )
            context={
                'status':"Otp has been successfully send to your mail"
            }
            return redirect('verify_otp')
        else:
            context={
                'status': "Email is not exists" 

            }
        return render(request,"admin_panel/send_otp.html",context)

    def get(self,request):
        return render(request,"admin_panel/send_otp.html")          

class verify_otp(View):
    def get(self,request):
        return render(request,'admin_panel/verify_otp.html')

    def post(self,request):
        context={}
        email = request.POST['email']
        otp = request.POST['otp']
        password = request.POST['password']
        if check_blank_or_null([email,otp,password]) and User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            print(otp)
            if forgetotp.objects.filter(code=otp,user=user,is_used=False,expire__gte=datetime.now()).exists():
                fo=forgetotp.objects.get(code=otp,user=user,is_used=False,expire__gte=datetime.now())
                fo.is_used=True
                fo.save()
                if fo.attempt < 5:
                    user=User.objects.get(email=email)
                    user.set_password(password)
                    user.save()
                    return redirect('login')

                    context['status']="password is successfully updated"
                else:
                    context['status']="Your attempt to reset password is complet"            
            else:
                fo=forgetotp.objects.get(user=User.objects.get(email=email))
                fo.attempt+=1
                fo.save()
                context['status']="Incorrect otp"
        else:
            context['status']="Email is not exists"        
        return render(request,'admin_panel/verify_otp.html',context)
    

def profile(request):

    form=Profile.objects.filter(user=request.user)
    context={
        'form':form
    }
    return render(request, 'admin_panel/profile.html',context)


class ChangePasswordView(View):
    def get(self, request):
        return render(request, 'admin_panel/change_password.html')

    def post(self,request,*args,**kwargs):
        user =request.user
        print('user',user)
        form = ChangePasswordForm(request.POST or None,user=request.user)
        if form.is_valid():
            conpassword = form.cleaned_data.get('conpassword')
            print('conpassword',conpassword)
            user.set_password(conpassword)
            user.save()
            #update_session_auth_hash(request,form.user)
            return HttpResponseRedirect('login')    
        return render(request, 'admin_panel/change_password.html',{'form':form})

# Create your views here.

import pyrebase

config={
    "apiKey": "AIzaSyBOVaM9DGt4gzKiPkPW_BU-qeAs03xqZzM",
    "authDomain": "myproject-f29ed.firebaseapp.com",
    "databaseURL": "https://myproject-f29ed-default-rtdb.firebaseio.com/",
    "projectId": "myproject-f29ed",
    "storageBucket": "myproject-f29ed.appspot.com",
    "messagingSenderId": "598630777243",
    "appId": "1:598630777243:web:0fd9115f041d30155be13e",
   #measurementId: "G-XX7QFM6YG2"
    }
firebase=pyrebase.initialize_app(config)
authe =firebase.auth()
database=firebase.database()

def index(request):
    name = database.child('Data').child('Name').get().val()
    id = database.child('Data').child('Id').get().val()
    subcriber = database.child('Data').child('Subs').get().val()
    types = database.child('Data').child('Types').get().val()

    context={
        "name":name,
        "id":id,
        "subcriber":subcriber,
        "types":types,
    }
    return render(request,'admin_panel/profile.html',context)


from fcm_django.models import FCMDevice
import firebase_admin 
from firebase_admin import credentials
from firebase_admin.messaging import Message, Notification
Message(
    notification=Notification(title="title", body="text", image="url"),
    topic="Optional topic parameter: Whatever you want",
)

from firebase_admin.messaging import Message
Message(
    data={
        "Nick" : "Mario",
        "body" : "great match!",
        "Room" : "Portugal VS Denmark"
   },
   topic="Optional topic parameter: Whatever you want",
)
from firebase_admin.messaging import Message
from fcm_django.models import FCMDevice

# You can still use .filter() or any methods that return QuerySet (from the chain)
device = FCMDevice.objects.all().first()
#send_message parameters include: message, dry_run, app

#device.send_message(Message(data={...}))










"""""
device=FCMDevice.objects.all().first()
device.sent_message("Title","Message")
device.sent_message(data={"test": "test"})
device.send_message(title="Title", body="Message", icon=..., data={"test": "test"})

def send_notification(user_id, title, message, data):
    try:
        device = FCMDevice.objects.filter(user=user_id).last()
        result = device.send_message(title=title, body=message, data=data, 
           sound=True)
        return result
    except:
        pass
"""""

class CustomerRegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=CustomerRegistrationForm()
        return render(request, 'admin_panel/register.html',{'form':form})

    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            #messages.success(request,'Congratulation!! Registered Successfully ')
            form.save()
            messages.success(request,"Congratulation!! Registered Successfully ")
            return redirect('login')
        return render(request, 'admin_panel/register.html',{'form':form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"admin_panel/login.html",{})

    def post(self,request,*args,**kwargs):
        context={}
        email = request.POST.get("email")	
        password = request.POST.get("password")
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"email and password is not exists")
        return render(request,"admin_panel/login.html",context)	

def logoutUser(request):
    logout(request)
    return redirect('login')

def destroy(request, id):
    if request.user.is_superuser==True:
        form=User.objects.get(id=id)
        form.delete()
        return redirect("user_management")
    else:
        return render(request,'admin_panel/permission.html')


def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file
        form = EditProfileForm(request.POST, instance=request.user)

        if profile_form.is_valid() and form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, 'Your profile update Successfully')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        
    context={'form':form,'profile_form':profile_form}

    return render(request,'admin_panel/edit-profile.html',context)
    
def user_deactivate(request, user_id):
    if request.user.is_superuser==True or request.user.is_admin==True:
        user = User.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        messages.success(request, "User account has been successfully deactivated!")
        return redirect('user_management')
    else:
        return render(request,'admin_panel/permission.html')


def user_activate(request, user_id):
    if request.user.is_superuser==True or request.user.is_admin==True:
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        messages.success(request, "User account has been successfully activated!")
        return redirect('user_management')
    else:
        return render(request,'admin_panel/permission.html')


def view_user(request, user_id):
    user=User.objects.get(pk=user_id)
    

import xlwt

from django.http import HttpResponse
#from django.contrib.auth.models import User

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Full Name','Email address','Status']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('full_name', 'email','is_active') 
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
