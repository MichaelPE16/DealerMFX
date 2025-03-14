"""
URL configuration for DealerApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Dealer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('singup/', views.singup, name = 'singup'),
    path('task/', views.task, name = 'task'),
    path('sigout/', views.signout, name = 'singout'),
    path('singin/', views.signin, name = 'singin'),
    path('create_vehicle/', views.create_vehicle, name = 'create_vehicle'),
    path('task/<int:vehicle_id>/', views.vehicle_details, name = 'vehicle_details'),
    path('task/<int:vehicle_id>/sell', views.sell, name = 'sell'),
    path('task/<int:vehicle_id>/delete', views.delete, name = 'delete'), 
    path('task/sold', views.vehicle_sold, name = 'sold'), 
]
