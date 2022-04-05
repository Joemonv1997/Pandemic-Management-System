from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm,UserForm
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,"home.html",{})
    
class LogInUser(TemplateView):
    form=UserForm
    def get(self,request,*args, **kwargs):
        return render(request,"login.html",{'form':self.form})
    def post(self,request,*args, **kwargs):
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )
        if user is None:
            return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect('/')