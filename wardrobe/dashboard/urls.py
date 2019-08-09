from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard',IndexView.as_view(), name='index'),
    path('',LoginView.as_view(),name='login'),
    path('linked',LinkedView.as_view(), name='linked'),
    path('add-automation',AddAutomation.as_view(), name='add_automation'),
    path('pending-approval-list',PendingApprovalList.as_view(),name='pending_approval_list'),
    path('database',Database.as_view(),name='database'),

]