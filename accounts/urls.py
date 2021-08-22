
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from.views import CustomerRegistrationView

urlpatterns = [
    path('',views.index,name="home"),
    path('home',views.index,name="home"),
    path('register/',views.CustomerRegistrationView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('user_management/',views.UserManagement,name="user_management"),
    path('profile/',views.profile,name="profile"),
    path('passwordchange/',views.ChangePasswordView.as_view(),name="passwordchange"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('delete/<int:id>',views.destroy,name="delete"),
    path('send_otp/',views.send_otp.as_view(),name="send_otp"),
    path('verify_otp/',views.verify_otp.as_view(),name="verify_otp"),
    path('blockuser/<int:user_id>',views.user_deactivate,name="blockuser"),
    path('unblockuser/<int:user_id>',views.user_activate,name="unblockuser"),
    path('viewuser/<int:user_id>',views.view_user,name="viewuser"),
    path('exportxls', views.export_users_xls, name='export_users_xls'),

]
