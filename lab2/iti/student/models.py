from django.db import models
from staff.models import *


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50, default='default_password')
    staffObj = models.ForeignKey(to='staff.Staff', on_delete=models.CASCADE)




    
   

    
