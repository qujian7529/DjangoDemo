DjangoDemo个人博客  

####1.项目创建　django-admin startproject DjangoDemo　　
生成项目目录  
manage.py:一个与这个项目一起工作的实用的命令行工具，可让你以各种方式与该 Django 项目进行交互  
__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包  
settings.py: 该文件包含了项目的默认设置，包括数据库信息、调试标志以及其他一些重要的变量。你可以通过这个文件设置/配置你的Django 项目。  
urls.py: Django中叫URLconf，是一个将URL模式映射到你的应用程序上的配置文件。或者也可以说是该 Django 项目的 URL 声明; 一份由Django驱动的网站"目录"。  
wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。  
####2.修改settings.py 
包含有关项目的配置信息，均大写。每个设置都有默认值，这些默认值定义在django/conf/global_settings.py。

ALLOWED_HOSTS = ['*']  

LANGUAGE_CODE = 'zh-Hans'  
TIME_ZONE = 'Asia/Shanghai'  

####3.新增app  
./manage.py startapp filmapp
