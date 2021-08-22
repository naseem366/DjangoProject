from django.forms import fields
from django.http import request
from django.shortcuts import redirect, render
from .models import Product
from django.views import View
from django.contrib import messages
from .forms import AddProductForm
from django.views.generic.edit import UpdateView
from django.views import generic
from django.urls import reverse_lazy
import os

# Create your views here.
class ProductListView(View):
    def get(self,request,*args,**kwargs):

        #products list
        products  = Product.objects.all().order_by('product_name') 
        context ={
            'products' : products,
        }
        return render(request,'admin_panel/product-management.html',context)

class AddProductView(View):
	def get(self,request):
		form=AddProductForm()
		return render(request,'admin_panel/add-product.html',{'form':form})
	def post(self, request):
		form=AddProductForm(request.POST,request.FILES)
		if form.is_valid():
			print("hello form datas")
			messages.success(request,'Congratulation !! Category  Add Successfully')
			form.save()
			print("form is save ")
			return redirect('product_management')
		else:
			form=AddProductForm()
			return render(request, 'admin_panel/add-product.html',{'form':form})

def EditProduct(request, pk):
    prod = Product.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.product_Image) > 0:
                os.remove(prod.product_Image.path)
            prod.product_Image = request.FILES['image']
        prod.product_name = request.POST.get('name')
        prod.amount = request.POST.get('price')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('product_management')

    context = {'prod':prod}
    return render(request, 'admin_panel/edit-product.html', context)

def destroy(request, id):  
    form = Product.objects.get(id=id)  
    form.delete()  
    return redirect("product_management") 



'''
def edit(request,id):
	editdata=Product.objects.get(id=id)
	if request.method=="POST":
		form=AddProductForm(request.POST,request.FILES,instance=editdata)
		if form.is_valid():
			form.save()
			return redirect("product_management")
	else:
		form=AddProductForm()
	template_name="admin_panel/edit-product.html"
	context={
		'AddProductForm':AddProductForm,
		'ProductModel':Product.objects.get(id=id),
	}
	return render(request,template_name,context)



class EditUpdateView(View):
	def get(self,request,pk):
		editdata=Product.objects.get(pk=pk)
		return render(request,'admin_panel/edit-product.html',{'editdata':editdata})

	def post(self, request,pk):
		data=Product.objects.get(pk=pk)
		form=AddProductForm(request.PUT,request.FILES,instance=data)
		if form.is_valid():
			form.save()
			print("Category Update Successfully")
			return redirect("category_management")
		else:		
			return render(request,'admin_panel/edit-product.html', {'data': data})


def destroy(request, id):  
    form = Product.objects.get(id=id)  
    form.delete()  
    return redirect("product_management") 


def edit_product(request,id):
	editdata=Product.objects.get(id=id)
	#print(form)
	return render(request,'admin_panel/edit-product.html',{'editdata':editdata})

def update_product(request,id):
	data = Product.objects.get(id=id)
	#print(data,"id is ")
	form = AddProductForm(request.POST,request.FILES,instance=data)  
	#print(form)
	if form.is_valid():
		form.save()
		print("hello form save")
		return redirect('product_management')
	return render(request,'admin_panel/edit-product.html', {'data': data})
    
'''