from django.db import models

from django.db import models
from django.contrib.auth.models import User, Group


class Country(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.Name}"


class Pandemic(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.Name}"


class State(models.Model):
    Country = models.ForeignKey(Country, models.CASCADE)
    State = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.State}"


class District(models.Model):
    State = models.ForeignKey(State, models.CASCADE)
    District = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.District}"


class Hospital(models.Model):
    type_choice=(('Government','Government'),
                    ("Private","Private"),
                    ("Semi Government","Semi Government"))
    District = models.ForeignKey(District, models.CASCADE)
    Hospital = models.CharField(max_length=1000, null=True, blank=True)
    type=models.CharField(max_length=25, choices=type_choice,null=True,blank=True)
    def __str__(self):
        return f"{self.Hospital}"


class Doctor(models.Model):
    Hospital = models.ForeignKey(Hospital, models.CASCADE)
    Name = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    Main=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.Name}"


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    FullName=models.CharField(max_length=100, null=True, blank=True)
    LastName=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(blank=True,null=True)
    Country=models.ForeignKey(Country, models.CASCADE)
    State=models.ForeignKey(State, models.CASCADE)
    District=models.ForeignKey(District,models.CASCADE)
    