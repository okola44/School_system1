from django.shortcuts import render
from .forms import StudentRegistrationForms

# Create your views here.
def register_student(request):
    form=StudentRegistrationForms()
    return render (request,"register_student.html",{"form":form})
