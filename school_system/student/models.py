from django.db import models
from django.db.models.enums import Choices


# Create your models here.
   

class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    EmailAdress=models.EmailField()
    DOB=models.DateField()
    age=models.PositiveSmallIntegerField()
    CountyorDistrict=models.CharField(max_length=20)
    National_ID=models.CharField(max_length=20)
    Student_ID=models.PositiveSmallIntegerField()
    language_choice=((u'E',u'English'),
                      (u'K',u'Kinyarwanda'),
                      (u'K',u'Kiswahili'),)
    language=models.CharField(max_length=2,choices=language_choice)
    Date_Of_Enrollment=models.DateField()
    Medical_Report=models.FileField()
    # ourse_name=models.ManyToManyField(Courses)
    Profile=models.ImageField(upload_to='head_shots')
    Serial_Number=models.CharField(max_length=15)
    Roll_number=models.PositiveSmallIntegerField()
    gender_choices=((u'M',u'male'),
    (u'F',u'female'),
    (u'O',u'Other'),)
    gender=models.CharField(max_length=1,choices=gender_choices)






    
