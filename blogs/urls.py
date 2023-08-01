from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_listing, name="blog_listing"),
    path('<slug>', views.blog_detail, name='blog_detail'),
    path('update/<slug>', views.update_blog, name='update_blog')
]


