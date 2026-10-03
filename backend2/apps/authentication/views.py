from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterationSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class RegisterationView(APIView):
    serializer_class=RegisterationSerializer
    permission_classes=[AllowAny]

