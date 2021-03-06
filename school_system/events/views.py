from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm
# def index(request):
#     return HttpResponse('hello')
class CalendarView(generic.ListView):
    model = Events
    template_name = 'event_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
def event(request, event_id=None):
    instance = Events()
    if event_id:
        instance = get_object_or_404(Events, pk=event_id)
    else:
        instance = Events()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('events:calendar'))
    return render(request, 'event_planner.html', {'form': form})

def edit_event(request,id):
    course=Events.objects.get(id=id)
    if request.method=="POST":
        form=EventForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
        return redirect("event_list",id=event.id)

    else:
        form=EventForm(instance=event)
        return render (request,"edit_event.html",{"form":form})

# def event_planner(request,id):
#     student=Events.objects.get(id=id)
#     return render(request,"event_planner.html",{"student":student})

# def event_list(request,id):
#     student=Events.objects.get(id=id)
#     if request.method=="POST":
#         form=EventForm(request.POST,instance=student)
#         if form.is_valid():
#             form.save()
#         return redirect("event_planner",id=student.id)

#     else:
#         form=EventForm(instance=student)
#         return render (request,"event_list.html",{"form":form})

    

