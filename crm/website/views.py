from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("home")