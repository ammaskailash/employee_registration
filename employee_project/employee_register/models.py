from typing import Any
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Roles(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    ecode = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)
