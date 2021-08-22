from django.urls import path
from productmanagement import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('product_management',views.ProductListView.as_view(),name="product_management"),
    path('add_product',views.AddProductView.as_view(),name="add_product"),
    #path('edit_product/<int:pk>',views.EditUpdateView.as_view(),name="edit_product"),
    path('edit_product/<int:pk>',views.EditProduct,name="edit_product"),
    #path('update/<int:id>',views.update_product,name="update"),
    path('deleteproduct/<int:id>',views.destroy,name="deleteproduct"),
   
]
