from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, PositiveSmallIntegerField


# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=10,blank=True,null=True)
    course_code=models.CharField(max_length=10,blank=True,null=True)
    course_schedule=models.FileField(blank=True,null=True)
    syllabus=models.TextField(blank=True,null=True)
    course_duration=models.CharField(max_length=20,blank=True,null=True)
    course_trainer=models.CharField(max_length=20,blank=True,null=True)
    time_in_hours=models.DurationField(blank=True,null=True)
    
  