from django.urls import path
from .views import trainer_form,trainers_list,edit_trainer,trainer_profile

urlpatterns=[path("register/",trainer_form, name="trainers_form"),
                path("list/",trainers_list,name="trainers_list"),
                path("profile/<int:id>/",trainer_profile,name="trainer_profile"),
                path("edit/<int:id>/",edit_trainer,name="edit_trainer"),
           
            
]