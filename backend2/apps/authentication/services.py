from .models import User,Role,UserRole
from django.db import transaction

@transaction.atomic
def create_user(*,username=None,password,email):
    user=User.objects.create(
        username=username,
        password=password,
        email=email
    )

    role = Role.objects.get(name="Customer")


    UserRole.objects.create(
        user=user,
        role=role,
        is_active=True,
        is_verified=True
    )

    return user