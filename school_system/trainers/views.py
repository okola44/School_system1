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

def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})

def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=Trainerforms(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
        return redirect("trainer_profile",id=trainer.id)

    else:
        form=Trainerforms(instance=trainer)
        return render (request,"edit_trainer.html",{"form":form})