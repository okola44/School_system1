
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from trainers.models import Trainer
from courses.models import Courses
from events.models import Events


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=("course_name","course_code")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=("title","description")


    