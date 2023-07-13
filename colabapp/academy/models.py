from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(User):

    bio = models.CharField(max_length = 500)

class Course(models.Model):
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 500)

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete = models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete = models.PROTECT)
    start_date = models.DateField()

class Student(User):
    pass
    
class Subscription(models.Model):
    student = models.ForeignKey(Student, on_delete = models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT)

