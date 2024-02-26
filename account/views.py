from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from utils.responses import SuccessResponse,FailureResponse
from utils.error_handler import error_handler
from rest_framework import status
from .mixin import EmailVerificationMixin
from .services import jwt_token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenRefreshView,TokenBlacklistView,TokenObtainPairView)


class AdminSignUpAPiView(APIView):
    authentication_classes=[]
    permission_classes=[]
    """
    Client signup account creation

    """
    @swagger_auto_schema(
            request_body=AccountCreationSerializer()
    )
    def post(self,request):
        try:
            serializer=AccountCreationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
          return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
    
class LoginApiView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.validated_data
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_404_NOT_FOUND)
        return SuccessResponse(data, status=status.HTTP_200_OK)


class EmailVerificationApiView(EmailVerificationMixin,APIView):
    permission_classes=[]
    authentication_classes=[]

    @swagger_auto_schema(
        request_body=EmailVerificationSerailaizer(),
        description='''This endpoint is used by both client an consellor
        usage:  This is email verification logic so it has two part on one api.
                when a user enter is email without otp and otp will be sent to the user
                after that the user will then send both the email and the sent otp the user will be verified.
                when a user otp time expires the user then send only his email to get a new otp.
                i recommend saving the email in a sharedpreference when the user first register.
                or u can also save it in sharedpreference during forgetpassword.
          '''
    )
    # @transaction.atomic
    def post(self, request,):
        return self.create(request)

class ResetPasswordApiView(APIView):
    permission_classes=[]
    authentication_classes=[]

    @swagger_auto_schema(
            request_body=ForgetPasswordInputSerializer
    )
    def post(self, request):
        try:
            #check to validate the otp of the user
            check_otp=EmailVerification.objects\
                .filter(email__iexact=request.data.get('email'),otp=request.data.get('otp')).first()
            if check_otp:
                serializer = ForgetPasswordInputSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return SuccessResponse("password created", status=status.HTTP_201_CREATED)
            else:
                return FailureResponse("otp or email is incorrect",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        try:
            res=super().post(request, *args, **kwargs)
        except Exception as e:
            return FailureResponse(error_handler(e), status=status.HTTP_400_BAD_REQUEST)
        return SuccessResponse(res.data,status=status.HTTP_200_OK)


class RefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            res=super().post(request, *args, **kwargs)
        except Exception as e:
            return FailureResponse(error_handler(e), status=status.HTTP_400_BAD_REQUEST)
        return SuccessResponse(res.data,status=status.HTTP_200_OK)
    
class UserProfile(APIView):
    def get(self,request):
        try:
           data=UserSerializer(request.user).data
           return SuccessResponse(data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
            
    @swagger_auto_schema(
            request_body=UserSerializer
    )
    def put(self,request):
        try:
           serializer=UserSerializer(request.user,data=request.data)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
            


        