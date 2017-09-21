# coding=utf-8

from django.conf.urls import url
from filmapp.views import *

# 主题路由
urlpatterns = [
	url(r'^$',index),
	url(r'^(?P<indexs>\D[a-z]{0,20})/$',index),
	
]

# 游客登录注册及注销
urlpatterns += [
	url(r'^login/$',login),
	url(r'^register/$',register),
	url(r'^loginout$',loginout),
]

# 评论
urlpatterns += [
	url(r'^technology/(?P<ids>\d{1,2})/$',comment),
]