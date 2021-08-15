from .models import Student
from django.shortcuts import render
from .forms import StudentRegistrationForms


# Create your views here.
def register_student(request):
    form=StudentRegistrationForms()
    return render (request,"register_student.html",{"form":form})

def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForms(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForms()

    return render(request,"register_student.html",{"form":form})

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})

    



