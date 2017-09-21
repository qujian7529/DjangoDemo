# coding=utf-8
"""
Django settings for film project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xu(6j7@m%pmyb48*&r0b=wgyj7@s9q&$y2+wka8(@)6a%4ffv!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 表示此Django站点可以投放的主机/域名的字符串列表。这是防止HTTP主机头部攻击的安全措施，即使在许多看似安全的Web服务器配置下也是如此。
# 可以是完全限定名称（例如“www.example.com”）
# 以期间开头的值可以用作子域通配符：'.example.com'将匹配example.com，www.example.com和example.com的任何其他子域。
# 值“*”匹配任何东西;在这种情况下，您有责任提供您自己对Host头的验证（可能在中间件中）;如果是这样，中间件必须首先列在MIDDLEWARE中
ALLOWED_HOSTS = ['*']


# Application definition

# 新增的app在这里添加
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filmapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'film.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 全局变量　
                # 'filmapp.static.static_setting',
            ],
        },
    },
]

WSGI_APPLICATION = 'film.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# 数据库的引入在这里  与自己的　　数据库、　用户名、密码　匹配，如果需要引入外部数据库需填写host ip和post 端口
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':'django.db.backends.mysql',
        'NAME':'django',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'',
        'POST':''
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 本地文件引入  路径拼接
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]
