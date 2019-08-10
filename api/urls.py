from django.urls import path,include
from .views import *

urlpatterns = [

	path('get-app_token',GetAppToken.as_view(), name="get_app_token"),

]