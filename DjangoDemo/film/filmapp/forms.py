# coding=utf-8

from django import forms


class LoginForm(forms.Form):
		username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),max_length=50,error_messages={"required": "username不能为空",})
		password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),	max_length=20,error_messages={"required": "password不能为空",})