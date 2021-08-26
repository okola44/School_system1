from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Student
from django.db.models.fields.files import ImageField


class StudentRegistrationForms(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
