from django.contrib.auth import get_user_model
from .models import Role,UserRole
from django.db import transaction
from .selectors import get_user_by_email
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
User=get_user_model()

@transaction.atomic
def create_user(*,email,username=None,password):
    user=User.objects.create(
        username=username,
        password=password,
        email=email
    )

    role=Role.objects.get(name="Customer")

    UserRole.objects.create(
        role=role,
        user=user,
        is_active=True,
        is_approved=True

    )

    return user

def login_user(*,email,password):
    user=get_user_by_email(email)

    if user is None:
        raise AuthenticationFailed('Invalid Email or Password')

    authenticated_user=authenticate(
        email=email,
        password=password
    )

    if not authenticated_user:
        raise AuthenticationFailed("Invalid Email or Password")

    refresh=RefreshToken.for_user(authenticated_user)

    return {
        "user": authenticated_user,
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }

