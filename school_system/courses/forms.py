from django import forms
from django.db import models
from django.forms import fields
from .models import Courses


class Coursesattributeform(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"