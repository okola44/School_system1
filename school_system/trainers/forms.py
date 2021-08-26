from django import forms
from django.db import models
from django.forms import fields
from .models import Trainer
from django.db.models.fields.files import ImageField

class Trainerforms(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"
