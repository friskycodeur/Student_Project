from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    subject_choices=[
        ('Maths','Mathematics'),
        ('Bio','Biology'),
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ]
    subject=models.CharField(max_length=9,choices=subject_choices,default='Maths')
    bookpdf=models.FileField(upload_to='media/')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    name=models.CharField(max_length=200)
    speaker=models.CharField(max_length=100)
    subject_choices=[
        ('Maths','Mathematics'),
        ('Bio','Biology'),
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ]
    subject=models.CharField(max_length=9,choices=subject_choices,default='Maths')
    video=models.FileField(upload_to='media/lectures')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=200)
    subject_choices=[
        ('Maths','Mathematics'),
        ('Bio','Biology'),
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ]
    subject=models.CharField(max_length=9,choices=subject_choices,default='Maths')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name