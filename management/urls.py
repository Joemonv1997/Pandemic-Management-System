from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="h"),
    path("login",views.LogInUser.as_view(),name="Login")
]
