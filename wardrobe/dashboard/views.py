from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import json


class IndexView(View):
	template_name='index.html'

	def get(self,request,*args, **kwargs):
		user=User.objects.all()
		user_list = json.dumps([u.username for u in user])
		return render(request,self.template_name,locals())

	def post(self,request):
		username=request.POST.get('username')
		password=request.POST.get('createpass')
		first_name=request.POST.get('fname')
		last_name=request.POST.get('lname')
		email_id=request.POST.get('emailid')
		user=User.objects.create(
			username=username,
			email=email_id,
			)
		user.set_password(password)
		user.first_name=first_name
		user.last_name=last_name
		user.save()
		return HttpResponseRedirect('/dashboard')

class LoginView(TemplateView):
	template_name='login.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())

	def post(self,request):
		username=request.POST.get('user')
		password=request.POST.get('passwd')
		user=authenticate(username=username, password=password)
		print(user)
		if user:
			login(request,user)
			return HttpResponseRedirect('/dashboard')

		else:
			return render(request,self.template_name,locals())
		
