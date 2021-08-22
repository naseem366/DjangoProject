from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import OrderPlaced
from accounts.models import *
from django.views import View
from datetime import date
# Create your views here.
def order_management(request):
	order_placed=OrderPlaced.objects.all()
	return render(request, 'admin_panel/order-management.html',{'order_placed':order_placed})

def filter_by_date(date):
    return OrderPlaced.objects.filter(post_date__year=date.year,
                                  post_date__month=date.month,
                                  post_date__day=date.day)

