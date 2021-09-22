from django.urls import path
from .views import course_attributes,courses_list,edit_courses,courses_details 

urlpatterns=[path("register/",course_attributes, name="course_attributes"),
            path("list/",courses_list,name="courses_list"),
            path("profile/<int:id>/",courses_details,name="courses_details"),
            path("edit/<int:id>/",edit_courses,name="edit_courses"),
            
 ]
           