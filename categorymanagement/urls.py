from django.urls import path
from categorymanagement import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('category_management',views.CatergoryListView.as_view(),name="category_management"),
    path('add_category',views.AddCatergoryView.as_view(),name="add_category"),
    path('edit_category/<int:id>',views.EditUpdateCategory,name="edit_category"),
    #path('update/<int:id>',views.update_category,name="update"),
    path('delete/<int:id>',views.destroy,name="delete"),
   
]