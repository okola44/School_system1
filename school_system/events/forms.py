from django import forms
from django.db import models
from django.forms import fields
from .models import Events


class Eventplannerform(forms.ModelForm):
    class Meta:
        model=Events
        fields="__all__"