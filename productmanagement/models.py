from categorymanagement.models import Category
from django.db import models

# Create your models here.

class Product(models.Model):
    #category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200,blank=True,null=True)
    product_Image=models.ImageField(default="",null=True,blank=True) 
    amount=models.IntegerField()
    created_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.product_name)