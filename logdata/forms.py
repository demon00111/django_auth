from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name','last_name','username','email']