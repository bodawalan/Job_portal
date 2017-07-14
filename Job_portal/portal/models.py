from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _



# Create your models here.
#suggestion model

class Suggestion(models.Model):
    Name=models.CharField(max_length=30, blank=True)
    Email=models.EmailField( null=True)
    Suggestion=models.TextField(max_length=400)

    def __str__(self):
        return self.Name

