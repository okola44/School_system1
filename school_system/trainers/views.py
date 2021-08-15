from django.shortcuts import render
from .forms import Trainerforms

# Create your views here.
def trainer_form(request):
    form=Trainerforms()
    return render (request,"trainers_form.html",{"form":form})

def trainer_form(request):
    if request.method=="POST":
        form=Trainerforms(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=Trainerforms()

    return render(request,"trainers_form.html",{"form":form})