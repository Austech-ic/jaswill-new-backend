from django.urls import path as url,re_path
from .views import (
                    AdminSignUpAPiView,
                    LoginApiView,
                    EmailVerificationApiView,
                    ResetPasswordApiView,
                    LogoutView,
                    RefreshTokenView,
                    UserProfile
                    )
urlpatterns = [
url('admin/sign-up/',AdminSignUpAPiView.as_view()),
url('admin/login/',LoginApiView.as_view()),
url('email-verification/',EmailVerificationApiView.as_view()),
url('reset-password/',ResetPasswordApiView.as_view()),
url('token/refresh/',RefreshTokenView.as_view()),
url('logout/',LogoutView.as_view()),
url("user/profile/",UserProfile.as_view())
]
