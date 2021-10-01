from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse 


class studentModelTestcase(TestCase):
    def setUp(self):
        self.student=Student(first_name='Happy',
                            last_name='Okola',
                            gender='F',
                            county_district='NAIROBI',
                            gurdians_name='Kimani',
                            grade='B',
                            age=20,
                            laptop_number=155
                            )

    def test_fullname_contains_first_name(self):
        # returns true of false
        self.assertIn(self.student.first_name,self.student.full_name())

    def test_fullname_contains_last_name(self):
        # returns true of false
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_student_year_of_birth(self):
        current_year = datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_register_student(self):
        url=reverse("register_student")
        data={"first_name":self.student.first_name,
                "last_name":self.student.last_name,
                "age":self.student.age,
                "county_district":self.student.county_district
                }
        request=self.client.post(url,data)
        self.assertEquals(request.status_code,200)

        




        


