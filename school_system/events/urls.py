from django.urls import path
from .views import event_planner 

urlpatterns=[path("register/",event_planner, name="event_planner"),]