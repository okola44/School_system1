from django.urls import path
from .views import event_planner,event_list 

urlpatterns=[path("register/",event_planner, name="event_planner"),
               path("list",event_list,name="event_list"),]