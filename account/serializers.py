from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model
from .models import EmailVerification
from django.db.models import Q
from rest_framework.views import APIView
User=get_user_model()

class AccountCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=[
            "username",
            "email",
            "password",
            "terms_condition"

        ]
        extra_kwargs={
            "password":{
                "write_only":True
            },
            "username":{
                "required":True
            },
        }

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise RuntimeError("email : This field already exist")
        else:
            return attrs
        
    def create(self, validated_data):
        user=User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class TokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": _("login provided credentials does not exist")
    }
    token_class = RefreshToken
    
    def validate_email(self,data):
        if User.objects.filter(Q(email__iexact=data)|Q(username__iexact=data)).exists():
            return data
        raise serializers.ValidationError("email does not exist")
        
class EmailVerificationSerailaizer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    otp=serializers.CharField(max_length=5,required=True)
            
class UserEmailVerificationSerailaizer(serializers.Serializer):
    email=serializers.EmailField(required=True,write_only=True)
      
class ForgetPasswordInputSerializer(serializers.Serializer):
    email=serializers.CharField(required=True,max_length=20)
    password=serializers.CharField(required=True, write_only=True)
    confirm_password=serializers.CharField(required=True,write_only=True)
    otp=serializers.CharField(required=True,write_only=True,max_length=6)

    def validate(self, attrs):
        if attrs['password']==attrs['confirm_password']:
            return attrs
        raise RuntimeError("password doesn't match")

    def create(self, validated_data):
        try:   
            new_password=validated_data.get('password')
            user=User.objects.get(email__iexact=validated_data['email'])
            user.set_password(new_password)
            user.confirm_password=user.password
            user.save()
        except Exception as e:
            raise serializers.ValidationError(e)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=[
            "username",
            "email"
        ]
        extra_kwargs={
            "email":{
                "read_only":True
            }
        }
