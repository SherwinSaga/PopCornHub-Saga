from django.db import models

# Create your models here.


class User(models.Model):
    # Add any additional user attributes here
    # Mao ra guro ni sa pagka karon
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)