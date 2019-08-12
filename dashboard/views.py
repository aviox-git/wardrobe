from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from api.models import *
import json
from django.contrib import messages
from django.http import JsonResponse

class LoginView(TemplateView):
	template_name='login.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())

	def post(self,request):
		username=request.POST.get('user')
		password=request.POST.get('passwd')
		user=authenticate(username=username, password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect('/dashboard')

		else:
			return render(request,self.template_name,locals())

class UserView(View):
	template_name='user.html'

	def get(self, request, *args, **kwargs):
		users = UserModel.objects.all()
		user_list = json.dumps([u.user.username for u in users])

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
		user_obj=UserModel(
			user=user,
			phone=request.POST.get('pnumber'),
			image=request.FILES.get('img'),
			dob=request.POST.get('dob'),
			gender=request.POST.get('gender')
			)
		user_obj.save()
		return HttpResponseRedirect('/dashboard')


class UserActive(View):

	def get(self, request):
		user_id = request.GET.get("user_id")
		User.objects.get(id=user_id).delete()
		messages.success(request,"user is successfully deleted")
		return HttpResponseRedirect('/dashboard')

	def post(self,request,*args, **kwargs):
		user_id = request.POST.get("id")
		user= User.objects.get(id=user_id)
		if user.is_active == True:
			user.is_active = False
		else:
			user.is_active = True
		user.save()
		return HttpResponseRedirect("/dashboard")

class UserEdit(View):
	template_name='user_edit.html'
	def get(self,request,userid):
		user_id=userid
		user_data=User.objects.get(id=user_id)
		
		return render(request, self.template_name, locals())

	def post(self,request,userid):
		user_id=userid
		first_name=request.POST.get('fname')
		last_name=request.POST.get('lname')
		email_id=request.POST.get('email')
		phone=request.POST.get('pnum')
		image=request.FILES.get('img')
		dob=request.POST.get('dob')
		gender=request.POST.get('gender')
		
		user_obj=User.objects.get(id=user_id)
		user_obj.first_name=first_name
		user_obj.last_name=last_name
		user_obj.email=email_id
		user_obj.usermodel.phone=phone
		user_obj.usermodel.image=image
		user_obj.usermodel.dob=dob
		user_obj.usermodel.gender=gender
		user_obj.save()
		return HttpResponseRedirect('/dashboard')


		
