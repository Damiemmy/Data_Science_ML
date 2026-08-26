from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterationSerializer,LoginSerializer,LoginResponseSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class=RegisterationSerializer
    permission_classes=[AllowAny]

class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        serializers= LoginSerializer(data=request.data)

        serializers.is_valid(
            raise_exception=True
        )

        response_serializer=LoginResponseSerializer(serializers.user_data)

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK
           
        )