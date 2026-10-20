from rest_framework import serializers
from .models import User
from .services import create_user

class RegisterationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,max_length=8)
    password2=serializers.CharField(write_only=True,max_length=8)

    class Meta:
        model=User
        fields=['email','username','password','password2']

    def validate_email(self,value):
        if User.objects.filter(email=value).exist():
            raise serializers.ValidationError("Email Already Exist in Database")
        return value.lower()

    def validate(self,attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError(' Password Do not Match')
        return attr

    def create(self,validated_data):
        validated_data.pop['password2']

        return create_user(
            username=validated_data.get("username"),
            password=validated_data["password"],
            email=validated_data["email"]
        )




