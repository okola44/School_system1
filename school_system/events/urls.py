from django.conf.urls import url
from .import views
from .views import edit_event
app_name = 'events'
urlpatterns = [
    # url(r'index/', views.index, name='index'),
    url(r'calendar', views.CalendarView.as_view(), name='calendar'),
    url(r'eventform', views.event, name='event_list'),
    url("edit/<int:id>/",edit_event,name="edit_event"),
  
]