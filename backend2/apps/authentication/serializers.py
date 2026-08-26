from rest_framework import serializers
from .models import User
from .services import create_user,login_user

class RegisterationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=[
            "email",
            "username",
            "password",
            "confirm_password"
        ]
    
    def validate_email(self,value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("Email Already Exists")
        return value.lower()

    def validate(self,attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({
                "Confirm Password":
                "Password do not match"
            })
        return attrs

    def create(self,validated_data):
        validated_data.pop("confirm_password")

        return create_user(
            email=validated_data["email"],
            username=validated_data.get("username"),
            password=validated_data["password"]
        )

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self,attrs):
        self.user_data=login_user(
            email=attrs["email"],
            password=attrs["password"]
        )
        return attrs

class UserSerializer(serializers.ModelSerializer):
    roles=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=[
            "id",
            "username",
            "email",
            "roles",
            "is_verified"
        ]
    
    def get_roles(self,obj):
        return[
            user_role.role.name
            for user_role in obj.user_roles.filter(is_active=True)
        ]

class LoginResponseSerializer(serializers.Serializer):
    user=UserSerializer()
    access=serializers.CharField()
    refresh=serializers.CharField()