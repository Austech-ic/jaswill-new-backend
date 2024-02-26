from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from utils.error_handler import error_handler
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import EmailVerification
from .serializers import EmailVerificationSerailaizer
import string,datetime
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from utils.responses import SuccessResponse,FailureResponse
import string
from django.utils.crypto import get_random_string
from rest_framework_simplejwt.tokens import RefreshToken

User=get_user_model()

class EmailVerificationMixin:

    def create(self,request):
        email=request.data.get('email',None)
        otp=request.data.get('otp',None)
        try:
            user=User.objects.filter(email__iexact=email).first()
            if user:
                '''
                This is email verification logic so it has two part on one api.
                when a user just registed he create an email verification for the user then send the user
                otp.so if he user forget the otp it will run the update method to resend a new otp to the user
                by checking if the user already exist.
                finally if the user enter the otp an is wrong it raise exception,when the user enter the right otp
                it check if it has not expired,if successfull the user will be verified.
                
                '''
                instance=EmailVerification.objects.filter(email__iexact=email).first()
                if instance and not otp:
                    instance_serializer = EmailVerificationSerailaizer(instance=instance,data=request.data)
                    instance_serializer.is_valid(raise_exception=True)
                    return self.perform_update(instance_serializer)
                elif not instance and not otp:
                    serializer = EmailVerificationSerailaizer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    return self.perform_create(serializer)
                else:
                    try:
                        user_data=EmailVerification.objects.get(email__iexact=email,otp=otp)
                        return self.can_do_verification(user_data,email)
                    except Exception as e:
                        return FailureResponse(error_handler("You entered wrong OTP code,please check it again")
                        ,status=status.HTTP_404_NOT_FOUND)
            return FailureResponse(error_handler("you have entered a wrong email"),
                        status=status.HTTP_404_NOT_FOUND)  
        except Exception as e:
            data={
                "message":error_handler(e),
                "status":"failed"     
            }
            raise ValidationError(data)
        

    def perform_create(self,serializer):
        otp=get_random_string(5,allowed_chars=string.digits)
        serializer.save(otp=otp)
        self.send_email(serializer.data)
        return SuccessResponse(serializer.data,status=status.HTTP_201_CREATED)
    
    def perform_update(self,instance):
        otp=get_random_string(5,allowed_chars=string.digits)
        instance.save(otp=otp)
        self.send_email(instance.data)
        return SuccessResponse(instance.data,status=status.HTTP_201_CREATED)
    
    def send_email(self,data):
            subject = 'Confirm Your Email Address'
            message = render_to_string('accounts/email_confirmation.html', {
            'otp':data['otp'],
        }) 
            from_email = settings.EMAIL_HOST_USER
            to_email = data['email']
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

    def can_do_verification(self,user_data,email):
        if user_data.date_generated + datetime.timedelta(seconds=300) > datetime.datetime.now(datetime.timezone.utc):
            user_detail=User.objects.get(email__iexact=email)
            return self.check_verification(user_detail)
        else:
            return FailureResponse("Verification Link Has Expired",
                   status=status.HTTP_400_BAD_REQUEST)

    def check_verification(self,user):
        if not user.is_verified:
            return self.not_verified(user)
        else:
            return SuccessResponse(self.jwt_token(user),status=status.HTTP_200_OK)                     

    def not_verified(self,user):
            user.is_verified=True
            user.save()
            return SuccessResponse(self.jwt_token(user),status=status.HTTP_200_OK)


    @staticmethod
    def jwt_token(user):
        data={}
        refresh=RefreshToken.for_user(user)   
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
    



