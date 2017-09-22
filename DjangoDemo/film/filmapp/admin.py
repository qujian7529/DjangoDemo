# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from filmapp.models import User,Article,Tag,Category

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
