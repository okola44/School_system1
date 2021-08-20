from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, PositiveSmallIntegerField


# Create your models here.
   

class Student(models.Model):
    first_name=models.CharField(max_length=10,blank=True,null=True)
    last_name=models.CharField(max_length=10,blank=True,null=True)
    gender_choices=((u'M',u'male'),
    (u'F',u'female'),
    (u'O',u'Other'),)
    gender=models.CharField(max_length=1,choices=gender_choices,blank=True,null=True)
    email_adress=models.EmailField(blank=True,null=True)
    # Phone_number=models.phone
    date_of_birth=models.DateField(blank=True,null=True)
    gurdians_name=models.CharField(max_length=20,blank=True,null=True)
    age=models.PositiveSmallIntegerField(blank=True,null=True)
    county_district=models.CharField(max_length=20,default="nairobi")
    national_id=models.CharField(max_length=20,blank=True,null=True)
    student_id=models.PositiveSmallIntegerField(blank=True,null=True)
    language_choice=((u'E',u'English'),
                      (u'K',u'Kinyarwanda'),
                      (u'K',u'Kiswahili'),)
    language=models.CharField(max_length=2,choices=language_choice,blank=True,null=True)
    date_of_enrollment=models.DateField(blank=True,null=True)
    medical_report=models.FileField(upload_to='documents/',blank=True,null=True)
    # ourse_name=models.ManyToManyField(Courses)
    profile=models.ImageField(upload_to='media/',null=True)
    serial_number=models.CharField(max_length=15,blank=True,null=True)
    roll_number=models.PositiveSmallIntegerField(blank=True,null=True)
    laptop_number=models.CharField(max_length=10,blank=True,null=True)
    grade=models.CharField(max_length=5,blank=True,null=True)

from django.db import models


    







    
