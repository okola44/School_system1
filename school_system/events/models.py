from django.db import models
class Events(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    start_time = models.DateTimeField(blank=True,null=True)
    end_time = models.DateTimeField(blank=True,null=True)
    venue=models.CharField(max_length=12,default="Bool",null=True,blank=True)
    event_planner=models.CharField(max_length=12,default="Samantha",null=True,blank=True)
  
 


    
    
    

    