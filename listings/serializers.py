from rest_framework import serializers
from .models import *

class BlogInputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=[
            "title",
            "body",
            "status",
            "image"
        ]
        extra_kwargs={
            "status":{
                "required":False
            }
        }

class BlogOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

class PropertyOutputSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=PropertyListing
        fields="__all__"
        depth=1

    def to_representation(self, instance):
        representation=super().to_representation(instance)
        image=ImageAsset.objects.select_related("property").filter(property=instance)
        representation['images']=ImageSerializer(image,many=True).data
        return representation


class PropertySerializer(serializers.ModelSerializer):
    image=serializers.ImageField(required=False,write_only=True)
    class Meta:
        model=PropertyListing
        fields="__all__"
        extra_kwargs={
            "status":{
                "required":False
            }
        }
     

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageAsset
        fields="__all__"
        depth=1

class ListingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ListingCategory
        fields="__all__"

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimony
        fields="__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutUs
        fields="__all__"

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model=Icon
        fields="__all__"

class OurserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurServices
        fields="__all__"

class OurserviceOutPutSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurServices
        fields="__all__"
        depth=1

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields="__all__"