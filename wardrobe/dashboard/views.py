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

	def post(request):
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return render(request,self.template_name)

class LinkedView(TemplateView):
	template_name='linked.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())


class AddAutomation(TemplateView):
	template_name='add_automation.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())


class PendingApprovalList(TemplateView):
	template_name='pending_approval_list.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())


class Database(TemplateView):
	template_name='database.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name,locals())