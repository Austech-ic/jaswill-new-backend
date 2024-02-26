import string
from django.utils.crypto import get_random_string
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


# @staticmethod
def check_verification(user):
          if not user.is_verified:
               raise AuthenticationFailed("Unauthorizied: User not Verified")


# @staticmethod
def check_isactive(user):
     if not user.is_active:
          raise AuthenticationFailed("access denied: You account have been disabled")
     

@staticmethod
def jwt_token(user):
    data={}
    refresh=RefreshToken.for_user(user)   
    data["refresh"] = str(refresh)
    data["access"] = str(refresh.access_token)
    return data