import bcrypt
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def register(request):
    if "user_id" in request.session:
        return redirect("/search")
    else:
        form = request.POST
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            password = form["password"]
            secure = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=form["f_name"], last_name = form["l_name"], email=form["email"], password=secure)
            request.session["user_id"] = user.id
        return redirect("/search")

def login(request):
    form = request.POST
    try:
        user = User.objects.get(email=form["log_email"])
    except:
        messages.error(request, 'Please check your login credentials')
        return redirect("/")
    
    if bcrypt.checkpw(form["log_password"].encode(), user.password.encode()) == False:
        messages.error(request, 'Please check your login credentials')
        return redirect("/")
    
    request.session["user_id"] = user.id
    return redirect("/search")

def logout(request):
    request.session.clear()
    return redirect("/")
