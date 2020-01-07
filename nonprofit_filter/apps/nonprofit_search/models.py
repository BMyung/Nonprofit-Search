from django.db import models
from apps.nonprofit_login.models import *

class Nonprofit(models.Model):
    name = models.CharField(max_length=255)
    ein = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    impact = models.CharField(max_length=255, default = "")
    website = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name = "nonprofits")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)