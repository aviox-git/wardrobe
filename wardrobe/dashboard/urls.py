from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('',LoginView.as_view(),name='login'),
	path('dashboard',IndexView.as_view(), name='index'),
]