# coding=utf-8

from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),max_length=50,error_messages={"required": "username不能为空",})
	password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),	max_length=20,error_messages={"required": "password不能为空",})


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),max_length=30,error_messages={"required": "username不能为空",})

	email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required",}),max_length=50,error_messages={"required": "email不能为空",})

	password = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password", "required": "required",}),max_length=30,error_messages={"required": "password不能为空",})


class CommentForm(forms.Form):

	# 评论
	content = forms.CharField(widget=forms.Textarea(attrs={"id":"comment","class": "message_input",
                                                           "required": "required", "cols": "25",
                                                           "rows": "5", "tabindex": "4"}),
                                                    error_messages={"required":"评论不能为空",})