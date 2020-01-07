from django.db import models
from django.core.validators import validate_email


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["f_name"]) < 2:
            errors["f_name"] = "First name should be at least two characters"
        if len(postData["l_name"]) < 2:
            errors["l_name"] = "Last name should be at least two characters"
        try:
            validate_email(postData["email"])
        except:
            errors["email"] = "Please enter a valid email"
        if len(postData["password"]) < 8:
            errors["password"] = "Please enter a password of at least 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_pass"] = "Please make sure the passwords match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()