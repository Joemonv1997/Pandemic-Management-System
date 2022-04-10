from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="h"),
    path("login", views.LogInUser.as_view(), name="Login"),
    path("logout", views.logoutuser, name="Logout"),
    path("register", views.RegisterUser.as_view(), name="register"),
    path("group",views.Groupcreate.as_view(),name="group"),
    path("countrycreate",views.Countrycreate.as_view(),name="country"),
    path("statecreate",views.Statecreate.as_view(),name="state"),
    path("districtcreate",views.Districtcreate.as_view(),name="district"),
    path("hospitalcreate",views.Hospitalcreate.as_view(),name="hospital"),
    path("doctorcreate",views.Doctorcreate.as_view(),name="doctor"),
    path("usercreate",views.Registercreate.as_view(),name="userregister"),
    path("userlist",views.users.as_view(),name="userlist"),
    path("usall",views.allusers.as_view(),name="usa"),
    path("usal",views.alluser.as_view(),name="us"),
    path("update/<int:id>",views.updateuser.as_view(),name="updateuser")

]
