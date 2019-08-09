
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',include('dashboard.urls')),
]