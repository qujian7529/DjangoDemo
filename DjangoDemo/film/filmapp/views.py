# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

# Django个人博客　
def index(request):
	return render(request,'index.html')

# 电影
def film(request):
	return

# 技术
def technology(request):
	return

# 旅游
def tourism(request):
	return

# 生活
def life(request):
	return

from filmapp.forms import LoginForm


# 登录

def login(request):
	if  request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username = username,password = password)
			if user is not None:
				return render(request,'')
			else:
				return render(request,)
# 注册
def register(request):
	return

# 注销
def loginout(request):
	return