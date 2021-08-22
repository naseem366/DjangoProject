from django import forms 
from django.forms import fields
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['product_name','product_Image','amount']  

    def clean(self):
        category_name = self.cleaned_data.get('category_name')
        category_image= self.cleaned_data.get('category_image')
        
        if not category_name or category_name == '':
            raise forms.ValidationError('category name is required')

        if category_image is None:
            raise forms.ValidationError('category image is required')

        return self.cleaned_data

