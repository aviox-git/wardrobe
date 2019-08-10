from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login


class IndexView(View):
	template_name='index.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())

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
		

class UserView(TemplateView):
	template_name='users.html'

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,locals())

class Adduser(TemplateView):
	template_name='add_user.html'

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,locals())

