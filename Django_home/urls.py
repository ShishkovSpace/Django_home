"""Django_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstApp import views

urlpatterns = [
    path('', views.homepage, name='home'),
    re_path(r'^firstpage', views.firstpage, name='firstpage'),
    re_path(r'^products/$', views.products),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
    re_path(r'^users/<int:user_id>/<str:name>/', views.users),
    re_path(r'^about/contact/', views.contact),
    re_path(r'^about', views.about),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
]
