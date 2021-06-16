from django.urls import path
from . import views

app_name ='App_blog'

urlpatterns = [
    path('',views.Bloglist.as_view(), name='blog_list'),
    path('write/',views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>', views.blog_details, name='blog_details'),
    path('likes/<pk>', views.liked, name='liked_post'),
    path('unlikes/<pk>', views.unliked, name='unliked_post'),
    path('my_blog/', views.Myblogs.as_view(), name='my_blogs'),
    path('edit_blog/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),

]
