from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db import models
class UserRegisterForm(models.Model):
	username=models.CharField(max_length=128, unique=True)
	email=models.CharField(max_length=128, unique=True)
	password=models.CharField(max_length=128)
	
    