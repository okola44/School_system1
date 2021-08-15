from django.urls import path
from .views import course_attributes  

urlpatterns=[path("register/",course_attributes, name="course_attributes"),]