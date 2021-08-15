from django.db import models

# Create your models here.
class Events(models.Model):
    venue=models.CharField(max_length=10,blank=True,null=True)
    event_id=models.CharField(max_length=10,blank=True,null=True)
    event_name=models.CharField(max_length=20,blank=True,null=True)
    event_duration=models.DurationField(blank=True,null=True)
    event_planner=models.CharField(max_length=20,blank=True,null=True)
    event_approved_by=models.CharField(max_length=20,blank=True,null=True)
    event_participants=models.TextField(blank=True,null=True)
    event_date_and_time=models.DateField(blank=True,null=True)


    
    
    

    