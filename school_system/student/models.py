from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, PositiveSmallIntegerField


# Create your models here.
   

class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    gender_choices=((u'M',u'male'),
    (u'F',u'female'),
    (u'O',u'Other'),)
    gender=models.CharField(max_length=1,choices=gender_choices)
    emailAdress=models.EmailField()
    # Phone_number=models.phone
    dob=models.DateField()
    gurdians_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    countyorDistrict=models.CharField(max_length=20)
    national_ID=models.CharField(max_length=20)
    student_ID=models.PositiveSmallIntegerField()
    language_choice=((u'E',u'English'),
                      (u'K',u'Kinyarwanda'),
                      (u'K',u'Kiswahili'),)
    language=models.CharField(max_length=2,choices=language_choice)
    date_of_enrollment=models.DateField()
    medical_Report=models.FileField()
    # ourse_name=models.ManyToManyField(Courses)
    profile=models.ImageField(upload_to='head_shots')
    serial_Number=models.CharField(max_length=15)
    roll_number=models.PositiveSmallIntegerField()
 
    laptop_number=models.CharField(max_length=10)
    grade=models.CharField(max_length=5)







    
