from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render

from management.models import Country
from .forms import UserRegistrationForm, UserForm,StateForm,DistrictForm,HospitalForm,DoctorForm,RegisterForm,ProfileForm
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group

# Create your views here.
def index(request):
    return render(request, "home.html", {})


class LogInUser(TemplateView):
    form = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, "login.html", {"form": self.form})

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect("/")


class RegisterUser(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect("/")
class Groupcreate(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "group.html")

    def post(self, request, *args, **kwargs):
        print(request.POST)
        group,created=Group.objects.get_or_create(name=request.POST["name"])
        if created:
            group.save()
            return redirect("/")
        return render(request, "group.html")


class Countrycreate(TemplateView):
    model=Country
    template_name="country_create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        country,created=Country.objects.get_or_create(Name=request.POST["name"])
        if created:
            country.save()
            return redirect("/")
        return render(request,self.template_name)


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return redirect("/login")
    
    return redirect("/")



class Statecreate(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "state_create.html",{'form':StateForm})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form=StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        return render(request,"state_create.html",{'form':form} )

class Districtcreate(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "district_create.html",{'form':DistrictForm})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form=DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        return render(request,"district_create.html",{'form':form} )

class Hospitalcreate(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "hospital_create.html",{'form':HospitalForm})

    def post(self, request, *args, **kwargs):
        form=HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        return render(request,"district_create.html",{'form':form} )


class Doctorcreate(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "doctor_create.html",{'form':DoctorForm})

    def post(self, request, *args, **kwargs):
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        return render(request,"doctor_create.html",{'form':form} )


class Registercreate(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "user_create.html",{'form':RegisterForm,'profile':ProfileForm,'hospital':DoctorForm})

    def post(self, request, *args, **kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        return render(request,"doctor_create.html",{'form':form} )