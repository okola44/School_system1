from django import forms
from django.db import models
from django.forms import fields
from .models import Trainer


class Trainerforms(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"
