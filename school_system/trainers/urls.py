from django.urls import path
from .views import trainer_form

urlpatterns=[path("register/",trainer_form, name="trainers_form"),]