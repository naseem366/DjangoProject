from rest_framework import serializers
from ..models import OrderPlaced
from productmanagement.models import Product

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model=OrderPlaced
		fields=['product','ordered_date','status']

