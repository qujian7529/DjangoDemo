DjangoDemo个人博客  

#### 1.项目创建　django-admin startproject DjangoDemo　　
生成项目目录  
- manage.py:一个与这个项目一起工作的实用的命令行工具，可让你以各种方式与该 Django 项目进行交互  
- __init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包  
-settings.py: 该文件包含了项目的默认设置，包括数据库信息、调试标志以及其他一些重要的变量。你可以通过这个文件设置/配置你的Django 项目。  
- urls.py: Django中叫URLconf，是一个将URL模式映射到你的应用程序上的配置文件。或者也可以说是该 Django 项目的 URL 声明; 一份由Django驱动的网站"目录"。  
+ wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。  
#### 2.修改settings.py 
包含有关项目的配置信息，均大写。每个设置都有默认值，这些默认值定义在django/conf/global_settings.py。

    LANGUAGE_CODE = 'zh-Hans'
    TIME_ZONE = 'Asia/Shanghai'  
    
      ALLOWED_HOSTS = ['*']  
#### 3.新增app  
    ./manage.py startapp filmapp
在filmapp新增urls.py 路由，建立一个测试路由并在views.py写好相应视图函数，进行测试
#### 4.简单测试
    ./manage.py runserver 0.0.0.0:8000
输入urls.py定义好的路径，检查是否能成功执行
#### 5.搭建个人博客架构
urls.py:

        from django.conf.urls import url
        from filmapp.views import *


        # 主题路由
        
        urlpatterns = [
          url(r'^$',index),
          url(r'^film/$',film),
          url(r'^technology/$',technology),
          url(r'^tourism/$',tourism),
          url(r'^life/$',life),
        ]
        
        # 游客登录注册及注销
        urlpatterns += [
          url(r'^login/$',login),
          url(r'^register/$',register),
          url(r'^loginout$',loginout),
        ]

views.py:

       from django.shortcuts import render,HttpResponse
       
       # Django个人博客　
       def index(request):
         return HttpResponse('Hello World')


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

       # 登录
       def login(request):
	       return

       # 注册
       def register(request):
	       return

       # 注销
       def loginout(request):
	       return
#### 6.本地静态路径static
settings.py:

	# 本地文件引入  路径拼接
	STATICFILES_DIRS = [
    		os.path.join(BASE_DIR,'static'),
	]
模板：

	TEMPLATES = [
	{ 
		...
		'DIRS': [
            		os.path.join(BASE_DIR,'templates'),
        	],
	},
	]
html:

	{% load static %}
	<img  src="{% static 'images/1.jpg' %}" />
运行测试

#### 7.login
filmapp目录下新建forms.py文件，将需要form验证的数据在此
forms  [http://www.cnblogs.com/btchenguang/archive/2012/08/27/2658598.html]
