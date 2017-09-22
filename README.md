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

#### 7.登录注册的详写
forms.py:

	class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),max_length=50,error_messages={"required": "username不能为空",})
	password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),	max_length=20,error_messages={"required": "password不能为空",})

	class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),max_length=30,error_messages={"required": "username不能为空",})

	email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required",}),max_length=50,error_messages={"required": "email不能为空",})

	password = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password", "required": "required",}),max_length=30,error_messages={"required": "password不能为空",})
views.py:

	from filmapp.forms import LoginForm,RegisterForm
	from filmapp.models import User
	from django.contrib import auth
	from django.contrib.auth.hashers import make_password
	from django.views.decorators.csrf import csrf_exempt,csrf_protect
	# 注册
	@csrf_exempt
	def register(request):
		if request.method == 'POST':
			register_form = RegisterForm(request.POST)
			print register_form
			if register_form.is_valid():
				print '+++++++++++++++++++++++'
				user = User.objects.create(
			    username=register_form.cleaned_data["username"],
			    email=register_form.cleaned_data["email"],
			    # 用户明文提交，不过我们是以加密形式保存密码，就用django提供的密码加密方法，这里用它默认的加密方式
			    password=make_password(register_form.cleaned_data["password"]),)
				user.save()
				return redirect(request.META['HTTP_REFERER'])
			else:
				return HttpResponse('失败的操作')	

		print '--------------------------------'
		return render(request,'register.html',locals())
		
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
	# 注销
	def loginout(request):
	try:
		# django提供注销功能
		logout(request)
	except Exception as e:
		print e
	return redirect()
models.py:

	class User(models.Model):
		#头像用图片类型
		avatar = models.ImageField(\
		upload_to='avatar/%Y/%m', default='avatar/default.png', \
		max_length=200, blank=True, null=True, verbose_name='用户头像')

		username = models.CharField(max_length =\
				     30,blank=True,null=True,verbose_name='用户名')
		password = models.CharField(max_length=100,blank=True,null=True,verbose_name='密码')
		email = models.EmailField(max_length=50,blank=True,null=True,verbose_name='邮箱地址')
		class Meta:
			verbose_name = '游客'
			verbose_name_plural = verbose_name
			ordering = ['-id']
		def __unicode__(self):
			return self.username
filmapp目录下新建forms.py文件，将需要form验证的数据在此
forms  [http://www.cnblogs.com/btchenguang/archive/2012/08/27/2658598.html]

#### 8.对页面路由的规整

urls.py:

	urlpatterns = [
		url(r'^$',index),
		url(r'^(?P<indexs>\D[a-z]{0,20})/$',index),
	
	]

views.py:
	
	def index(request,indexs = ''):
		return render(request,'index.html',locals())

html:

	<!-- 导航 -->
	<nav class="navbar navbar-default" role="navigation">
		  <div class="container">
		    <!-- Brand and toggle get grouped for better mobile display -->
		    <div class="navbar-header">
		      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-brand-centered">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		      </button>
		      <div class="navbar-brand navbar-brand-centered" style="font-size: 25px;width: 250px;margin-left: -120px" >
		      	<a href="/0" >Django个人博客</a>
		      </div>
		    </div>

		    <!-- Collect the nav links, forms, and other content for toggling -->
		    <div class="collapse navbar-collapse" id="navbar-brand-centered">
		      <ul class="nav navbar-nav">
		        <li><a href="/film">电影推荐</a></li>
		        <li><a href="/technology">技术达人</a></li>
		      </ul>
		      <ul class="nav navbar-nav navbar-right">
		        <li><a href="/tourism">我的生活</a></li>
		        <li><a href="/life">旅游心情</a></li>		        
		      </ul>
		    </div><!-- /.navbar-collapse -->
		  </div><!-- /.container-fluid -->
	</nav>
使这几个页面能点击跳转
#### 9.打印文章

models.py:

	# 标签
	class Tag(models.Model):
		name = models.CharField(max_length = 100,verbose_name = '标签')
		class Meta:
			verbose_name = '标签'
			verbose_name_plural = verbose_name
			ordering = ['-id']
		def __unicode__(self):
			return self.name
	# 分类
	class Category(models.Model):
		name = models.CharField(max_length = 100,verbose_name = '分类')
		class Meta:
			verbose_name = '分类'
			verbose_name_plural = verbose_name
			ordering = ['-id']
		def __unicode__(self):
			return self.name
	# 文章
	class Article(models.Model):
		# 作者
		author = models.ForeignKey(User,verbose_name='用户',default = '')
		# 文章标题
		title = models.CharField(max_length=50, verbose_name='文章标题')
		# 描述
		desc = models.CharField(max_length=50, verbose_name='文章描述')
		# 内容
		content = models.TextField(verbose_name='文章内容')
		# 时间
		date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

		# 分类　一个分类对多个文章
		category = models.ForeignKey(Category,default = '',verbose_name='分类')
		# 标签　一个文章可以多个标签　一个标签可以多个　文章
		tages = models.ManyToManyField(Tag,blank=True,verbose_name='标签')
		class Meta:
			verbose_name = '文章'
			verbose_name_plural = verbose_name
			ordering = ['-id']
		def __unicode__(self):
			return self.title
管理文章，添加几篇文章
admin.py:
	
	from filmapp.models import User,Article,Tag,Category

	admin.site.register(User)
	admin.site.register(Article)
	admin.site.register(Tag)
	admin.site.register(Category)

改造一下views
views.py:
	
	# Django个人博客　
	def index(request,indexs = ''):
		if indexs == 'film':
			film(request)
		elif indexs == 'technology':
			article_lists = technology(request)
		elif indexs == 'tourism':
			tourism(request)
		elif indexs == 'life':
			life(request)
		print locals()
		return render(request,'index.html',locals())

	# 电影
	def film(request):
		return

	# 技术
	def technology(request):
		# order_by 方法对这个返回的 queryset 进行排序。排序依据的字段是 created_time，即文章的创建时间。
		article_lists = Article.objects.all().order_by('-date_publish')
		print article_lists
		return article_lists


html:

	<ul>
		{%for article in article_lists %}
			<li>
				<div>{{article.title}}</div>
				<div>{{article.desc}}</div>
				<div>{{article.content}}</div>
			</li>
		{% empty %}
			<div class="no-post">暂时还没有发布的文章！</div>
		{% endfor %}
	</ul>

#### 10.详情页面

forms.py:

	class CommentForm(forms.Form):

	# 评论
	content = forms.CharField(widget=forms.Textarea(attrs={"id":"comment","class": "message_input",
                                                           "required": "required", "cols": "25",
                                                           "rows": "5", "tabindex": "4"}),
                                                    error_messages={"required":"评论不能为空",})
models.py:
	
	# 文章
	class Article(models.Model):
		# 文章标题
		title = models.CharField(max_length=50, verbose_name='文章标题')
		# 描述
		desc = models.CharField(max_length=50, verbose_name='文章描述')
		# 内容
		content = models.TextField(verbose_name='文章内容')
		# 时间
		date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')


	# 评论
	class Comment(models.Model):
		commtime = models.Datecontent = models.TextField(verbose_name='评论内容')
		# 评论那篇文章
		user = models.ForeignKey(User,blank = True,null = True, verbose_name ='评论人')
		article = models.ForeignKey(Article,blank= True,null =True,verbose_name = '文章')TimeField(auto_now_add =True,verbose_name ='发布时间')

html:
	
	#文章部分
	{% if indexs == '' %}
	...
	{% elif  indexs == 'film' %}
	...
	{% elif indexs == 'technology' %}
	...
	 	<div class="col-md-12" style="color:#fff">
			<ul>
				<li>
					<div style="height: 200px;width: 100%;border-top:3px solid red;border-bottom: 1px solid #ccc;">
	 					<h1>主题部分</h1>
	 					<div class="row">
	 						<div class="col-md-2">
	 							<div><span>日期</span><span>评论</span></div>
	 							<div><span>链接</span></div>
	 						</div>
	 						<div class="col-md-10">
	 							<div>简介</div>
	 							
	 						</div>
	 					</div>
				</li>
			</ul>
		</div>
	{% elif indexs == 'tourism' %}
	...
	{% elif indexs == 'life' %}
	...
	{% endif %}
		
