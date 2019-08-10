from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	
	path('',LoginView.as_view(),name='login'),
	path('dashboard',IndexView.as_view(), name='index'),
    path('users',UserView.as_view(), name='users'),
    path('add-user', Adduser.as_view(), name='add_user'),
]