from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Users(AbstractBaseUser):
    user = models.CharField

