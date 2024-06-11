from django.shortcuts import render
from .models import *
from .serializers import *
from drf_yasg.openapi import IN_QUERY, Parameter
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from utils.responses import FailureResponse,SuccessResponse
from rest_framework import status
from utils.error_handler import error_handler
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class BlogApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(
            request_body=BlogInputSerializer
    )
    def post(self,request):
        try:
            serializer=BlogInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(BlogOutputSerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=Blog.objects.all()
            return SuccessResponse(BlogOutputSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
# class GetBlogApiView(APIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     def get(self,request):
#         try:
#             queryset=Blog.objects.filter(status="draft").all()
#             return SuccessResponse(BlogOutputSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class SingleBlogApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        try:
            instance=Blog.objects.get(pk=pk)
            return SuccessResponse(BlogOutputSerializer(instance).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
            request_body=BlogInputSerializer
    )
    def put(self,request,pk):
        try:
            instance=Blog.objects.get(pk=pk)
            serializer=BlogInputSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(BlogOutputSerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=Blog.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Blog deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class TestimonyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(
            request_body=TestimonySerializer
    )
    def post(self,request):
        try:
            serializer=TestimonySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(TestimonySerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=Testimony.objects.all()
            return SuccessResponse(TestimonySerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
# class GetTestimonyApiView(APIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     parser_classes=[JSONParser,MultiPartParser,FormParser]
    
#     def get(self,request):
#         try:
#             queryset=Testimony.objects.all()
#             return SuccessResponse(TestimonySerializer(queryset,many=True).data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class SingleTestimonyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        try:
            instance=Testimony.objects.get(pk=pk)
            return SuccessResponse(TestimonySerializer(instance).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
            request_body=TestimonySerializer
    )
    def put(self,request,pk):
        try:
            instance=Testimony.objects.get(pk=pk)
            serializer=TestimonySerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(TestimonySerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=Testimony.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("Blog deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleCategoryApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]
        
    @swagger_auto_schema(
            request_body=ListingCategorySerializer
    )
    def put(self,request,pk):
        try:
            instance=ListingCategory.objects.get(pk=pk)
            serializer=ListingCategorySerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(ListingCategorySerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            instance=ListingCategory.objects.get(pk=pk)
            instance.delete()
            return SuccessResponse("category deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class CategoryApiView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
        
    @swagger_auto_schema(
            request_body=ListingCategorySerializer
    )
    def post(self,request):
        try:
            serializer=ListingCategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            return SuccessResponse(ListingCategorySerializer(data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            queryset=ListingCategory.objects.all()
            return SuccessResponse(ListingCategorySerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
# class GetCategoryApiView(APIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]

#     def get(self,request):
#         try:
#             queryset=ListingCategory.objects.all()
#             return SuccessResponse(ListingCategorySerializer(queryset,many=True).data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class PropertyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
            request_body=PropertySerializer
    )
    def post(self,request):
        try:
            serializer=PropertySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            image=serializer.validated_data.pop("image",None)
            data=serializer.save()
            #save image 
            if image:
                ImageAsset.objects.create(property=data,image=image)
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            manual_parameters=[
                Parameter("category",IN_QUERY,type="int",required=False)   
            ]
    )
    def get(self,request):
        try:
            category=request.GET.get("category",None)
            queryset=PropertyListing.objects.all()
            if category:
                queryset=queryset.filter(category__pk=category)
            return SuccessResponse(PropertyOutputSerilaizer(queryset,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

# class CreatePropertyApiView(APIView):
#     parser_classes=[JSONParser,MultiPartParser,FormParser]
#     permission_classes=[IsAuthenticatedOrReadOnly]

#     @swagger_auto_schema(
#             request_body=PropertySerializer
#     )
#     def post(self,request):
#         try:
#             serializer=PropertySerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             image=serializer.validated_data.pop("image",None)
#             data=serializer.save()
#             #save image 
#             if image:
#                 ImageAsset.objects.create(property=data,image=image)
#             return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

#     @swagger_auto_schema(
#             manual_parameters=[
#                 Parameter("category",IN_QUERY,type="int",required=False)   
#             ]
#     )
#     def get(self,request):
#         try:
#             category=request.GET.get("category",None)
#             queryset=PropertyListing.objects.all()
#             if category:
#                 queryset=queryset.filter(category__pk=category)
#             return SuccessResponse(PropertyOutputSerilaizer(queryset,many=True).data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class SinglePropertyApiView(APIView):
    parser_classes=[JSONParser,MultiPartParser,FormParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        try:
            instance=PropertyListing.objects.get(pk=pk)
            return SuccessResponse(PropertyOutputSerilaizer(instance).data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            request_body=PropertySerializer
    )
    def put(self,request,pk):
        try:
            instance=PropertyListing.objects.get(pk=pk)
            serializer=PropertySerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            image=serializer.validated_data.pop("image",None)
            data=serializer.save()
            #save image 
            if image:
                #delete the image associated to that instance
                ImageAsset.objects.filter(property=instance).delete()
                #save new image
                ImageAsset.objects.create(property=data,image=image)
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            instance=PropertyListing.objects.get(pk=pk)
            #delete the image associated to that instance
            ImageAsset.objects.filter(property=instance).delete()
            instance.delete()
            return SuccessResponse("Property Deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
class ContactUsApiView(APIView):
    parser_classes=[JSONParser,FormParser,MultiPartParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
            request_body=ContactUsSerializer,
            operation_id="image"
    )
    def post(self,request):
        try:
            serializer=ContactUsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            data=ContactUs.objects.order_by("-id").first()
            new_data=ContactUsSerializer(data).data
            return SuccessResponse(new_data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
# class GetContactUsApiView(APIView):

#     def get(self,request):
#         try:
#             data=ContactUs.objects.order_by("-id").first()
#             new_data=ContactUsSerializer(data).data
#             return SuccessResponse(new_data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleContactUsApiView(APIView):
    parser_classes=[JSONParser,FormParser,MultiPartParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(request_body=ContactUsSerializer)
    def put(self,request,pk):
        try:
            data=ContactUs.objects.get(pk=pk)
            serializer=ContactUsSerializer(instance=data,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            data=ContactUs.objects.get(pk=pk)
            data.delete()
            return SuccessResponse("contact us deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class AboutUsApiView(APIView):
    parser_classes=[JSONParser,FormParser,MultiPartParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
            request_body=AboutUsSerializer,
            operation_id="image"
    )
    def post(self,request):
        try:
            serializer=AboutUsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            data=AboutUs.objects.order_by("-id").first()
            new_data=AboutUsSerializer(data).data
            return SuccessResponse(new_data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
# class GetAboutUsApiView(APIView):

#     def get(self,request):
#         try:
#             data=AboutUs.objects.order_by("-id").first()
#             new_data=AboutUsSerializer(data).data
#             return SuccessResponse(new_data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleAboutUsApiView(APIView):
    parser_classes=[JSONParser,FormParser,MultiPartParser]

    @swagger_auto_schema(request_body=AboutUsSerializer)
    def put(self,request,pk):
        try:
            data=AboutUs.objects.get(pk=pk)
            serializer=AboutUsSerializer(instance=data,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            data=AboutUs.objects.get(pk=pk)
            data.delete()
            return SuccessResponse("about us deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class OurServiceApiView(APIView):
    parser_classes=[JSONParser,FormParser,MultiPartParser]
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
            request_body=OurserviceSerializer,
           
    )
    def post(self,request):
        try:
            serializer=OurserviceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            data=OurServices.objects.order_by("-id").first()
            new_data=OurserviceOutPutSerializer(data).data
            return SuccessResponse(new_data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
        
# class GetOurservicesApiView(APIView):

#     def get(self,request):
#         try:
#             data=OurServices.objects.order_by("-id").first()
#             new_data=OurserviceOutPutSerializer(data).data
#             return SuccessResponse(new_data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class SingleOurserviceContactUsApiView(APIView):
    parser_classes=[JSONParser,FormParser,MultiPartParser]

    @swagger_auto_schema(request_body=OurserviceSerializer)
    def put(self,request,pk):
        try:
            data=OurServices.objects.get(pk=pk)
            serializer=OurserviceSerializer(instance=data,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessResponse(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            data=OurServices.objects.get(pk=pk)
            data.delete()
            return SuccessResponse("our services deleted",status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)

class IconApiView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self,request):
        try:
            data=Icon.objects.all()
            new_data=IconSerializer(data,many=True)
            return SuccessResponse(new_data.data,status=status.HTTP_200_OK)
        except Exception as e:
            return FailureResponse(error_handler(e),status=status.HTTP_400_BAD_REQUEST)
