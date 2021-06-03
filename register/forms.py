from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Register(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username","email","password1","password2"]
