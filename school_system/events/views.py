from .models import Events
from django.shortcuts import render
from .forms import Eventplannerform

# Create your views here.
def event_planner(request):
    form=Eventplannerform()
    return render (request,"event_planner.html",{"form":form})

def event_planner(request):
    if request.method=="POST":
        form=Eventplannerform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=Eventplannerform()

    return render(request,"event_planner.html",{"form":form})

def event_list(request):
    events=Events.objects.all()
    return render(request,"event_list.html",{"events":events})

