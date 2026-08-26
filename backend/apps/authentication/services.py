from .models import User,UserRole,Role
from django.db import transaction
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from .selectors import get_user_by_email

@transaction.atomic
def create_user(*,username=None,email,password):
    user=User.objects.create(
        email=email,
        password=password,
        username=username,
    )

    role=Role.objects.get(name="Customer")

    UserRole.objects.create(
        user=user,
        role=role,
        is_active=True,
        is_approved=True
    )

    return user






    # user = get_user_by_email(email)

    # if user is None:
    #     raise AuthenticationFailed("Invalid email or password.")

    # authenticated_user = authenticate(
    #     email=email,
    #     password=password,
    # )

    # if authenticated_user is None:
    #     raise AuthenticationFailed("Invalid email or password.")

    # if not authenticated_user.is_active:
    #     raise AuthenticationFailed("Account is inactive.")

    # refresh = RefreshToken.for_user(authenticated_user)

    # return {
    #     "user": authenticated_user,
    #     "access": str(refresh.access_token),
    #     "refresh": str(refresh),
    # }

def login_user(*,email,password):
    user=get_user_by_email(email)

    if user is None:
        return ValidationFailed("Invalid Email or Password")
    
    authenticated_user= authenticate(
        email=email,
        password=password
    )

    if not authenticated_user:
        return ValidationFailed("Invalid Email or Password")

    refresh=RefreshToken.for_user(authenticated_user)

    return{
        "user":authenticated_user,
        "access":str(refresh.access_token),
        "refresh":str(refresh)
    }