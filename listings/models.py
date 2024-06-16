from django.db import models
import uuid
import re
from .constant import PROPERTY_TYPE,STATUS
SPECIAL_CHARS_REGEX = "[^a-zA-Z0-9 \n\.]"
class ListingCategory(models.Model):
    name=models.CharField(max_length=100,null=False)
# Create your models here.
class Blog(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    id=models.UUIDField(primary_key=True,editable=False,db_index=True,default=uuid.uuid4)
    title=models.TextField(null=True)
    body=models.TextField(null=False,blank=False)
    status=models.CharField(choices=STATUS,default="published",max_length=10)
    image=models.ImageField(upload_to=upload_to,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class PropertyListing(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,db_index=True,default=uuid.uuid4)
    title=models.CharField(max_length=500,null=False)
    description=models.TextField()
    city=models.CharField(max_length=500,null=False)
    category=models.CharField(max_length=500,null=True)
    content=models.TextField()
    location=models.CharField(max_length=500,null=False)
    status=models.CharField(choices=STATUS,default="active",max_length=20)
    property_ype=models.CharField(max_length=200,choices=PROPERTY_TYPE)
    price=models.DecimalField(max_digits=10,decimal_places=0)
    no_bedroom=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

class ImageAsset(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to)
    property=models.ForeignKey(PropertyListing,on_delete=models.CASCADE,null=True,blank=True)

class Testimony(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    name=models.TextField()
    comment=models.TextField()
    status=models.CharField(choices=STATUS,default="draft",max_length=10)
    image=models.ImageField(upload_to=upload_to,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class AboutUs(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to,null=True)
    about=models.TextField()

class Icon(models.Model):
    name=models.CharField(max_length=500)
    icon=models.URLField()

class OurServices(models.Model):
    icon=models.ForeignKey(Icon,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=500)
    content=models.TextField()

class ContactUs(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to,null=True)
    content=models.TextField(null=True)
    location=models.CharField(max_length=500,null=True)
    phone_number=models.TextField(null=True)
    whatapp_link=models.URLField(null=True)

class Device(models.Model):
    name=models.CharField(max_length=30,null=False)

class MostViewPage(models.Model):
    name=models.CharField(max_length=200,null=False)