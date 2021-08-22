from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['email','full_name','date_joined','last_login','is_active','is_admin']
    list_filter = ('is_admin','is_active','date_joined',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','city','phone_number','profile_image']

@admin.register(forgetotp)
class forgetotpAdmin(admin.ModelAdmin):
    list_display = ("user",'code','is_used','expire','attempt')

@admin.register(UserAddress)
class forgetotpAdmin(admin.ModelAdmin):
    list_display = ("user",'name','address','city','state','zipcode')
