from django.db import models


# Create your models here.
from staff.models import *


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    address = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    staff_id = models.ForeignKey(to='staff.Staff',on_delete=models.CASCADE)