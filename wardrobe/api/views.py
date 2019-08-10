# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.authentication import BaseAuthentication,BasicAuthentication, SessionAuthentication, TokenAuthentication
from django.conf import settings
from rest_framework import views
# Create your views here.

class GetAppToken(views.APIView):

	def get(self, request):
		pass
