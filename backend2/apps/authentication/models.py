from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=20,blank=True,null=True,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    is_verified=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    object= UserManager()

    def __str__(self):
        return self.email