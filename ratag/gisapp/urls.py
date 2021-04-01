from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include
from .models import *


app_name = 'gisapp'

urlpatterns = [

    path('', views.Sites_list.as_view(), name='Sites_list'),
    path('site/<int:pk>', views.Site_detail.as_view(), name='Site_detail'),
    path('hazard/<int:pk>', views.Hazard_detail.as_view(), name='Hazard_detail'),
    path('create_hazard/', views.Create_Hazard.as_view(), name='Create_hazard'),

    path('load_sites/', views.load_sites, name='load_sites'),

]
