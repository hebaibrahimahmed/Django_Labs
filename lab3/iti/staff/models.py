from django.db import models


# Create your models here.
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    address = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)