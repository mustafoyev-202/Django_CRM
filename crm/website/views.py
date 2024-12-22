from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Home view
def home(request):
    if request.method == "POST":
        # Get username and password from POST request
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("home")
        else:
            # Authentication failed
            messages.warning(request, "Invalid username or password")
            return redirect("home")
    else:
        # Render the home page
        return render(request, "home.html", {})


# Logout view
def logout_user(request):
    logout(request)
    messages.warning(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account was created for {username}")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})
