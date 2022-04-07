from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="h"),
    path("login", views.LogInUser.as_view(), name="Login"),
    path("logout", views.logoutuser, name="Logout"),
    path("register", views.RegisterUser.as_view(), name="register"),
    path("group",views.Groupcreate.as_view(),name="group"),
    path("countrycreate",views.Countrycreate.as_view(),name="country")
]
