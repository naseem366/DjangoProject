from django.db import models
from productmanagement.models import Product
# Create your models here.
STATUS_CHOICES=(

('Completed','Completed'),
('Cancel','Cancel'),
('Pending','Pending'),

	)

class OrderPlaced(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	ordered_date=models.DateTimeField(auto_now_add=True)
	status=models.CharField(choices=STATUS_CHOICES,max_length=50,default='Pending')

