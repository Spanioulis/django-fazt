from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)

class Tasks(models.Model):
    title = models.CharField(max_legnth=200)
    description = models.TextField
    person = models.ForeignKey(Person, on_delete=models.CASCADE)