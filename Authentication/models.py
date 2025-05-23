from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40, primary_key=True, null=False)
    password = models.CharField(max_length=40, null=False)
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, max_length=40,  null=False)
