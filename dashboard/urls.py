from django.contrib import admin
from django.urls import path
from dashboard import views
from .views import *

urlpatterns = [
	path('',LoginView.as_view(),name='login'),

	# ===============  Users ====== #

	path('dashboard',UserView.as_view(), name='index'),
	path('active-delete',UserActive.as_view(),name='active_delete'),
	path('user-edit/<int:userid>',UserEdit.as_view(),name='user_edit'),
]