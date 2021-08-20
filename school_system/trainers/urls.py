from django.urls import path
from .views import trainer_form,trainers_list

urlpatterns=[path("register/",trainer_form, name="trainers_form"),
                 path("list/",trainers_list,name="trainers_list"),
           
            
]