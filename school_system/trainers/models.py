from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=10,blank=True,null=True)
    last_name=models.CharField(max_length=10,blank=True,null=True)
    gender_choices=((u'M',u'male'),
    (u'F',u'female'),
    (u'O',u'Other'),)
    gender=models.CharField(max_length=1,choices=gender_choices,)
    email_adress=models.EmailField(blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    class_name=models.CharField(max_length=10)
    # Phone_number=models.phone
    date_of_hire=models.DateField(blank=True,null=True)
    age=models.PositiveSmallIntegerField(blank=True,null=True)
    profile=models.ImageField(upload_to='images/',blank=True,null=True)
    county_district=models.CharField(max_length=20,default="nairobi")
    national_id=models.CharField(max_length=20,blank=True,null=True)
    language_choice=((u'E',u'English'),
                      (u'K',u'Kinyarwanda'),
                      (u'K',u'Kiswahili'),)
    language=models.CharField(max_length=2,choices=language_choice,blank=True,null=True)
    contract=models.FileField(upload_to="documents/",blank=True,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   
    
   
   
   
   