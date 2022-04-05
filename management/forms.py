from dataclasses import fields
from django.contrib.auth.models import User,Group
from django.forms import Form,CharField,ImageField,IntegerField,IntegerField,ModelChoiceField
from .models import State,Country,Pandemic,District,Hospital
from django import forms
from django.contrib.auth.models import User
    
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

    
class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
    		    'username', 
    		    'password', 
    		    'email', 
    		    'first_name', 
    		    'last_name'
    	] 

class PandemicForm(forms.ModelForm):
	class Meta:
		model=Pandemic
		fields="__all__"

class CountryForm(forms.ModelForm):
	class Meta:
		model=Country
		fields="__all__"