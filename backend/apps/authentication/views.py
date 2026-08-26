from rest_framework.generics import CreateAPIView
from .serializers import RegisterationSerializer,LoginSerializer,LoginResponseSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status




class RegisterView(CreateAPIView):
    serializer_class=RegisterationSerializer
    permission_classes=[AllowAny]


# class LoginView(APIView):

#     permission_classes = [AllowAny]

#     def post(self, request):

#         serializer = LoginSerializer(
#             data=request.data
#         )

#         serializer.is_valid(
#             raise_exception=True
#         )

#         # return Response(
#         #     serializer.user_data,
#         #     status=status.HTTP_200_OK,
#         # )
#         response_serializer = LoginResponseSerializer(
#             serializer.user_data
#         )
#         return Response(
#             response_serializer.data,
#             status=status.HTTP_200_OK,
#         )




class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response_serializer=LoginResponseSerializer(serializer.user_data)
        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK
        )
