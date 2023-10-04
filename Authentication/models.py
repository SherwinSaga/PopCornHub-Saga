from django.db import models

# Create your models here.


class User(models.Model):
    # Add any additional user attributes here
    # Mao ra guro ni sa pagka karon
    username = models.CharField(max_length=45, primary_key=True, null=False)
    password = models.CharField(max_length=45, null=False)
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    email = models.EmailField(unique=True, max_length=45,  null=False)
