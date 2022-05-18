from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'password1', 'password2']
