from django.shortcuts import render,redirect
from .forms import Coursesattributeform
from .models import Courses

# Create your views here.
def course_attributes(request):
    form=Coursesattributeform()
    return render (request,"course_attributes.html",{"form":form})

def course_attributes(request):
    if request.method=="POST":
        form=Coursesattributeform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=Coursesattributeform()

    return render(request,"course_attributes.html",{"form":form})

def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"courses_list.html",{"courses":courses})


def courses_details(request,id):
    course=Courses.objects.get(id=id)
    return render(request,"courses_details.html",{"course":course})

def edit_courses(request,id):
    course=Courses.objects.get(id=id)
    if request.method=="POST":
        form=Coursesattributeform(request.POST,instance=course)
        if form.is_valid():
            form.save()
        return redirect("courses_details",id=course.id)

    else:
        form=Coursesattributeform(instance=course)
        return render (request,"edit_courses.html",{"form":form})