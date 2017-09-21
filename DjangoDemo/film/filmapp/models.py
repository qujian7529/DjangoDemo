# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

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
	commtime = models.DateTimeField(auto_now_add =True,verbose_name ='发布时间')
	content = models.TextField(verbose_name='评论内容')
	# 评论那篇文章
	user = models.ForeignKey(User,blank = True,null = True, verbose_name ='评论人')
	article = models.ForeignKey(Article,blank= True,null =True,verbose_name = '文章')


