from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),             # Home/login page
    path("logout", views.logout_user, name="logout"),  # Logout page
]
