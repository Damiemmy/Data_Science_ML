from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    username=models.CharField(
        unique=True,
        blank=True,
        null=True,
        max_length=50
    )
    email=models.CharField(
        unique=True
    )
    is_verified=models.BooleanField(
        default=False
    )

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    obj=UserManager()

    def __str__(self):
        return self.email

class Role(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_roles")
    role=models.ForeignKey(Role,on_delete=models.CASCADE,related_name="user_roles")
    is_active=models.BooleanField(default=True)
    is_approved=models.BooleanField(default=True)
    assigned_at=models.DateTimeField(auto_now_add=True)
