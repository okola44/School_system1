from django.urls import path
from .views import course_attributes,courses_list 

urlpatterns=[path("register/",course_attributes, name="course_attributes"),
             path("list/",courses_list,name="courses_list"),
 ]
           