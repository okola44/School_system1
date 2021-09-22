from django.shortcuts import render
from student.models import Student
from courses.models import Courses
from trainers.models import Trainer
from events.models import Events

# Create your views here.
def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Courses.objects.count()
    events=Events.objects.count()
    data={"students":students,"trainers":trainers,"courses":courses,"events":events}
    return render(request,"home.html",data)



