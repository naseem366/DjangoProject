from django.urls import path
from ordermanagement import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('order_management',views.order_management,name="order_management"),
    #path('product_management',views.product_management,name="product_management"),
    path('orderview',views.filter_by_date,name="orderview"),
    #path('edit_product/<int:pk>',views.EditUpdateView.as_view(),name="edit_product"),
    #path('edit_product/<int:pk>',views.EditProduct,name="edit_product"),
    #path('update/<int:id>',views.update_product,name="update"),
    
]
