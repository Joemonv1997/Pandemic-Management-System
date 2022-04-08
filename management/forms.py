from dataclasses import fields
from django.contrib.auth.models import User, Group
from django.forms import (
    Form,
    CharField,
    ImageField,
    IntegerField,
    IntegerField,
    ModelChoiceField,
)
from .models import Doctor, State, Country, Pandemic, District, Hospital,Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]


class PandemicForm(forms.ModelForm):
    class Meta:
        model = Pandemic
        fields = "__all__"


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = "__all__"


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields ="__all__"

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields=("Hospital",'Main')


class RegisterForm(forms.ModelForm):
    # email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ('username','password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=("user",)