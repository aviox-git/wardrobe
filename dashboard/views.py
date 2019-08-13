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
import datetime

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
		try:
			username=request.POST.get('username')
			password=request.POST.get('createpass')
			first_name=request.POST.get('fname')
			last_name=request.POST.get('lname')
			email_id=request.POST.get('emailid')
			dob=request.POST.get('dob')
			phone=request.POST.get('pnumber')
			image=request.FILES.get('img')
			gender=request.POST.get('gender')

			dob=datetime.datetime.strptime(dob,"%d-%m-%Y")
			user=User.objects.create(
				username=username,
				email=email_id,
				)
			user.set_password(password)
			user.first_name=first_name
			user.last_name=last_name
			user.save()
			print(user, phone,image,gender)
			user_obj=UserModel(
				user=user,
				image=image,
				dob=dob,
				gender=gender
				)
			if phone:
				user_obj.phone = phone
			user_obj.save()
		except Exception as e:
			raise e
		return HttpResponseRedirect('/dashboard')


class UserActive(View):

	def get(self, request):
		user_id = request.GET.get("user_id")
		print('user',user_id)
		print('user objects',User.objects.get(id=user_id))
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
		date=user_data.usermodel.dob.strftime("%d-%m-%Y")
		print(date)
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
		print(dob)
		date=datetime.datetime.strptime(dob,"%d-%m-%Y")
		
		user_obj=User.objects.get(id=user_id)
		user_obj.first_name=first_name
		user_obj.last_name=last_name
		user_obj.email=email_id
		if phone:
			user_obj.usermodel.phone=phone
		if image:
			user_obj.usermodel.image=image
		user_obj.usermodel.dob=date
		user_obj.usermodel.gender=gender
		user_obj.save()
		user_obj.usermodel.save()
		return HttpResponseRedirect('/dashboard')


		
