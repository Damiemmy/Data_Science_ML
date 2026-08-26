from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    username=models.CharField(
        blank=True,
        null=True,
        unique=True,
        max_length=20
    )
    email=models.EmailField(
        unique=True,
        max_length=50,
    )

    is_verified=models.BooleanField(
        default=False
    )

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]

    object= UserManager()

    def __str__(self):
        return self.email

class Role(models.Model):
    name=models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user=models.ForeignKey(
        User,on_delete=models.CASCADE,
        related_name='user_roles'
    )
    role=models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='user_roles'
    )
    is_active=models.BooleanField(
        default=False
    )
    is_approved=models.BooleanField(
        default=False
    )
    assigned_at=models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role"],
                name="unique_user_role",
            )
        ]
        ordering = ["-assigned_at"]
    
    def __str__(self):
        return f"{self.user.email} → {self.role.name}"
