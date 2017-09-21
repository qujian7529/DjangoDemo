# coding=utf-8

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