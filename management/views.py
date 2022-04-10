from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from management.models import Country, Doctor, Hospital,Profile
from .forms import UserRegistrationForm, UserForm,StateForm,DistrictForm,HospitalForm,DoctorForm,RegisterForm,ProfileForm
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
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
        return render(request, "user_create.html",{'form':UserCreationForm,'profile':ProfileForm,'hospital':DoctorForm})

    def post(self, request, *args, **kwargs):
        form=UserCreationForm(request.POST)
        profile=ProfileForm(request.POST)
        Doctor=DoctorForm(request.POST)
        if form.is_valid():
            u=form.save()
            p=profile.save(commit=False)
            p.user=u
            p.save()
            d=Doctor.save(commit=False)
            d.Name=u
            d.save()

            return redirect("/")
        
        return render(request,"user_create.html",{'form':RegisterForm,'profile':ProfileForm,'hospital':DoctorForm})

class users(TemplateView):
    def get(self, request, *args, **kwargs):
        doctor=Doctor.objects.all().values("Name__id","Name__username","Name__profile__FullName","Name__profile__LastName","Hospital__Hospital","Name__profile__State__State","Main")
        return render(request, "user_list.html",{'doctors':doctor})

class updateuser(TemplateView):
    def get(self, request, *args, **kwargs):
        u=User.objects.get(id=kwargs['id'])
        p=Profile.objects.get(user=kwargs['id'])
        h=Doctor.objects.get(Name=kwargs['id'])
        ProfileFm=ProfileForm(instance=p)
        Doctorm=DoctorForm(instance=h)
        return render(request, "user_create.html",{'profile':ProfileFm,'hospital':Doctorm})

class allusers(TemplateView):
    def get(self, request, *args, **kwargs):
        all_users=User.objects.all().values("username")
        return JsonResponse({"all_users":list(all_users)})


class alluser(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "users_all.html") 