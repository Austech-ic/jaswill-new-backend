from django.utils.crypto import get_random_string
import string
from .models import EmailVerification
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

def send_emails(email):
        try:
            otp=get_random_string(5,allowed_chars=string.digits)
            subject = 'Confirm Your Email Address'
            message = render_to_string('accounts/email_confirmation.html', {
            "otp":otp
        })
            from_email = settings.EMAIL_HOST_USER
            to_email = email
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            #save the email and the otp to email verification table
            EmailVerification.objects.filter(email=email).delete()
            EmailVerification.objects.create(email=email,otp=otp)
        except Exception as e:
             raise RuntimeError("error in sending email:{}".format(e))
             return None



def jwt_token(user):
    data={}
    refresh=RefreshToken.for_user(user)   
    data["refresh"] = str(refresh)
    data["access"] = str(refresh.access_token)
    return data