from django.contrib import admin
from .models import Role,UserRole,User


#Register your models here.
class UserInfo(admin.ModelAdmin):
    list_display=["email","username"]

admin.site.register(User,UserInfo)
admin.site.register(Role)
admin.site.register(UserRole)