from django import forms 
from django.forms import fields
from .models import Category

class AddCategoryForm(forms.Form):
    category_name  = forms.CharField()
    category_image = forms.ImageField()

    def clean(self):
        category_name = self.cleaned_data.get('category_name')
        category_image= self.cleaned_data.get('category_image')
        
        if not category_name or category_name == '':
            raise forms.ValidationError('category name is required')

        if category_image is None:
            raise forms.ValidationError('category image is required')

        return self.cleaned_data


'''
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
'''
