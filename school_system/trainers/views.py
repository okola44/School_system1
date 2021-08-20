from .models import Trainer
from django.shortcuts import render,redirect
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
            return redirect("trainers_form")
        else:
            print(form.errors)
    else:
        form=Trainerforms()

    return render(request,"trainers_form.html",{"form":form})

def trainers_list(request):
    trainers=Trainer.objects.all()

    return render(request,"trainers_list.html",{"trainers":trainers})