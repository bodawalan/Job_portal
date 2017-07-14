from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import ModelForm
from .models import Suggestion
from .import views
from django.core import validators
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings


class Sugesstion_Form(forms.ModelForm):
    class Meta:
        model=Suggestion
        fields=[
            'Name',
            'Email',
            'Suggestion',

        ]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)