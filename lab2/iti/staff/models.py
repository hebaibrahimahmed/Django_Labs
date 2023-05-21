from django.db import models

# Create your models here.

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Password = models.CharField(max_length=50, default='default_password')
    email = models.EmailField()
