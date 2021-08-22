from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200,blank=True,null=True)
    category_image=models.ImageField(upload_to='Category',null=True,blank=True)
    created_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.category_name)

