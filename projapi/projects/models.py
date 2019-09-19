from django.db import models
from datetime import date

# Create your models here.

# Model for Projects - Add class with class attributes


class FA(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Projects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    department = models.CharField(max_length=12)
    status = models.CharField(max_length=3)
    fa = models.ManyToManyField(FA)

    def __str__(self):
        return self.name+" "+self.status


