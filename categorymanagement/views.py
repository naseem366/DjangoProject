from django.shortcuts import redirect, render
from django.http import *
from .models import Category
from django.views import View
from django.contrib import messages
from .forms import AddCategoryForm
import os

# Create your views here.
class CatergoryListView(View):
    def get(self,request,*args,**kwargs):

        #category list
        categories  = Category.objects.all().order_by('category_name') 
        context ={
            'categories' : categories,
        }
        return render(request,'admin_panel/category-management.html',context)


class AddCatergoryView(View):
    def get(self,request,*args,**kwargs):
                
        form = AddCategoryForm()
        context = {
            'form' : form
        }
        return render(request,'admin_panel/add-category.html',context)

    def post(self,request,*args,**kwargs):
        form = AddCategoryForm(request.POST,request.FILES)
        context = {
            'form' : form,
            }
        
        if form.is_valid():
            data = form.cleaned_data       
            category_name = data['category_name']
            category_image= request.FILES.get('category_image')
            category_obj  = Category(category_name=category_name,category_image=category_image)
            category_obj.save()
            return HttpResponseRedirect('category_management')    
        return render(request,'admin_panel/add-category.html',context)


def EditUpdateCategory(request, id):
    prod = Category.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.category_image) > 0:
                os.remove(prod.category_image.path)
            prod.category_image = request.FILES['category_image']
        prod.category_name = request.POST.get('category_name')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('category_management')

    context = {'prod':prod}
    return render(request, 'admin_panel/edit-category.html', context)


def destroy(request, id):  
    form = Category.objects.get(id=id)  
    form.delete()  
    return redirect("category_management") 

'''
def edit_category(request,id):
	#category=request.category
	form=Category.objects.get(id=id)
	print(form)
	return render(request,'admin_panel/edit-category.html',{'form':form})

def update_category(request,id):
	employee = Category.objects.get(id=id)
	print(employee,"id is ")
	form = AddCategoryForm(request.POST,request.FILES,instance=employee)  
	print(form)
	if form.is_valid():
		form.save()
		return redirect('category_management')
	return render(request,'admin_panel/edit-category.html', {'employee': employee})
    #return render(request, 'admin_panel/edit-category.html', {'employee': employee})

class EditCatergoryView(View):
    def get(self,request,*args,**kwargs):
                
        category_id = self.kwargs['pk']
        try:
            category = Category.objects.get(id=category_id)
        except:
            return HttpResponse(status=404)

        form = EditCategoryForm()
        return render(request,'admin_panel/edit-category.html',{'category': category,'form': form})

    def post(self,request,*args,**kwargs):
        category_id = self.kwargs['pk']
        try:
            category = Category.objects.get(id=category_id)
        except:
            return HttpResponse(status=404)

        form = EditCategoryForm(request.POST,request.FILES, context= {'category_id': category_id})    
        if form.is_valid():
            data = form.cleaned_data 
            category_name = data['category_name']
            category_image= request.FILES.get('category_image')
            category.category_name = category_name
            if category_image is not None:
                category.category_image = category_image
            category.save()
            return HttpResponseRedirect('category_management')         

        return render(request,'admin_panel/edit-category.html',{'category': category,'form':form})







class AddCategoryView(View):
	def get(self,request):
		form=AddCategoryForm()
		return render(request,'admin_panel/add-category.html',{'form':form})
	def post(self, request):
		form=AddCategoryForm(request.POST,request.FILES)
		if form.is_valid():
			print("hello form datas")
			messages.success(request,'Congratulation !! Category  Add Successfully')
			form.save()
			print("form is save or not ")
			return redirect('category_management')
		else:
			form=AddCategoryForm()
			return render(request, 'admin_panel/add-category.html',{'form':form})

def EditUpdateCategory(request, id):
    prod = Category.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.category_image) > 0:
                os.remove(prod.category_image.path)
            prod.category_image = request.FILES['image']
        prod.category_name = request.POST.get('name')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('category_management')

    context = {'prod':prod}
    return render(request, 'admin_panel/edit-category.html', context)










'''

