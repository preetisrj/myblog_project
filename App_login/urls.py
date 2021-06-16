
from django.urls import path
from . import views

app_name = 'App_login'
urlpatterns = [

   path('signup/',views.sign_up, name='signup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='pass_change'),
    path('changepic/', views.addprofile_pic, name='addprofile_pic'),
    path('update_profilepic/', views.change_pro_pic, name='change_pro_pic'),
]
