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
    District = models.ForeignKey(District, models.CASCADE)
    Hospital = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.Hospital}"


class Doctor(models.Model):
    Hospital = models.ForeignKey(Hospital, models.CASCADE)
    Name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.Name}"


# class Patients(models.Model):
