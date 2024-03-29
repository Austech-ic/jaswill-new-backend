from django.urls import path as url,re_path
from .views import (
                    BlogApiView,
                    GetBlogApiView,
                    SingleBlogApiView,
                    TestimonyApiView,
                    GetTestimonyApiView,
                    SingleTestimonyApiView,
                    SingleCategoryApiView,
                    CategoryApiView,
                    GetCategoryApiView,
                    PropertyApiView,
                    CreatePropertyApiView,
                    SinglePropertyApiView,
                    ContactUsApiView,
                    OurServiceApiView,
                    IconApiView,
                    AboutUsApiView,
                    GetAboutUsApiView,
                    GetContactUsApiView,
                    GetOurservicesApiView,
                    SingleAboutUsApiView,
                    SingleContactUsApiView,
                    SingleOurserviceContactUsApiView
                    )
urlpatterns = [
url("blog/",BlogApiView.as_view()),
url("blogs/",GetBlogApiView.as_view()),
url("blog/<uuid:pk>/",SingleBlogApiView.as_view()),
url("testimony/",TestimonyApiView.as_view()),
url("testimonies/",GetTestimonyApiView.as_view()),
url("testimony/<int:pk>/",SingleTestimonyApiView.as_view()),
url("category/",CategoryApiView.as_view()),
url("category/<int:pk>/",SingleCategoryApiView.as_view()),
url("categories/",GetCategoryApiView.as_view()),
url("property/",CreatePropertyApiView.as_view()),
url("properties/",PropertyApiView.as_view()),
url("property/<uuid:pk>/",SinglePropertyApiView.as_view()),

#____________________---------------------__________________
url("contact/",ContactUsApiView.as_view()),
url("contacts/",GetContactUsApiView.as_view()),
url("contact/<int:pk>/",SingleContactUsApiView.as_view()),
url("our_service/",OurServiceApiView.as_view()),
url("our_services/",GetOurservicesApiView.as_view()),
url("our_service/<int:pk>/",SingleOurserviceContactUsApiView.as_view()),
url("about/",AboutUsApiView.as_view()),
url("abouts/",GetAboutUsApiView.as_view()),
url("about/<int:pk>/",SingleAboutUsApiView.as_view()),
url("icons/",IconApiView.as_view()),
]