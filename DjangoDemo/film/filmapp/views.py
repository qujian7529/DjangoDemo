# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

# Django个人博客　
def index(request,indexs = ''):

	return render(request,'index.html',locals())

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

from django.contrib import auth
from filmapp.forms import LoginForm,RegisterForm,CommentForm
from filmapp.models import User,Comment
from django.contrib.auth.hashers import make_password
# 登录
@csrf_exempt
def login(request):

	if  request.method == 'POST':
		login_form = LoginForm(request.POST)
		# 是否是有效的对象句柄
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = auth.authenticate(username = username,password = password)
			# 未找到用户

			if user is not None:
				return render(request,'login.html',{'logerr':'登录验证失败'})
			# 找到用户
			else:
				return HttpResponseRedirect(request.GET.get('next','/'))
		
		else:
			return HttpResponse('失败的操作')	
	# 如果不是post提交就跳转到登录页面
	# 未post请求
	else:
		login_form = LoginForm()
	return  render(request,'login.html',locals())
# 注册
@csrf_exempt
def register(request):
	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		print register_form
		if register_form.is_valid():
			user = User.objects.create(
                    username=register_form.cleaned_data["username"],
                    email=register_form.cleaned_data["email"],
                    # 用户明文提交，不过我们是以加密形式保存密码，就用django提供的密码加密方法，这里用它默认的加密方式
                    password=make_password(register_form.cleaned_data["password"]),)
			user.save()
			return redirect(request.META['HTTP_REFERER'])
		else:
			return HttpResponse('失败的操作')	
	
	return render(request,'register.html',locals())

# 注销
def loginout(request):
	try:
		# django提供注销功能
		logout(request)
	except Exception as e:
		print e
	return redirect()


def comment(request,ids):
	if request.method == 'POST':
		comm_form = CommentForm(request.POST)
		if comm_form.is_valid():
			comm =  Comment.objects.create(
				content = comm_form.cleaned_data['content']
				)
			comm.save()
		else:
			return HttpResponse('失败的评论')
	return redirect(request.META['HTTP_REFERER'])