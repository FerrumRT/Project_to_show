from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

def index(request):
    return render(request, "index.html", {"title": "Home page"})

def log_out(request):
    logout(request)
    return redirect('/')

def log_in(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        try:
            the_user = User.objects.filter(Q(email=request.POST.get("email", "")) | Q(username=request.POST.get("email", "")))[0]
            user = authenticate(username=the_user.username, password=request.POST.get("password", ""))
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Success login")
                return redirect("/")
            else:
                messages.add_message(request, messages.ERROR, "Wrong username or password")
        except:
            messages.add_message(request, messages.ERROR, "Wrong username or password")
        return redirect("/login")
    return render(request, "login.html", {"title":"Sign in"})

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        if len(User.objects.filter(Q(email=request.POST.get("email", "")) | Q(username=request.POST.get("username", ""))))!=0:
            messages.add_message(request, messages.ERROR, "User with this email or username already exists")
            return redirect("/login")
        password = request.POST.get("password", "")
        re_password = request.POST.get("re_password", "")
        print(password, re_password)
        if password == re_password:
            new_user = User()
            new_user.first_name = request.POST.get("name", "")
            new_user.email = request.POST.get("email", "")
            new_user.username = request.POST.get("username", "")
            new_user.set_password(request.POST.get("password", ""))
            new_user.save()
            messages.add_message(request, messages.SUCCESS, "Success registration")
            return redirect("/login")
        else:
            messages.add_message(request, messages.ERROR, "Passwords doesnt match")
    return render(request, "register.html", {"title":"Sign up"})