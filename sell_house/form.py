from django.db.models import fields
from django.forms import ModelForm, models
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SellForm(ModelForm):
    class Meta:
        model= Post
        fields="__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username",'email','password1',"password2"]
