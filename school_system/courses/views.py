from django.shortcuts import render
from .forms import Coursesattributeform

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
