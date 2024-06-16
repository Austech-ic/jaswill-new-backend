from listings.models import Device,MostViewPage
from django.utils.deprecation import MiddlewareMixin

class DeviceTrackerMiddleware(MiddlewareMixin):
        
    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        user_agent=request.META.get('HTTP_USER_AGENT', '').lower()
        if request.path != "/":
            if "ios" in user_agent:
                Device.objects.create(
                    name="Mobile"
                )
            if "mac os" in user_agent:
                Device.objects.create(
                    name="Web"
                )
            if "android" in user_agent:
                Device.objects.create(
                    name="Mobile"
                )
            if "windows" in user_agent:
                Device.objects.create(
                    name="Web"
                )

            # Code to be executed for each request/response after
        # the view is called.
        return response
    

class MostViewPageMiddleware(MiddlewareMixin):
        
    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        user_agent=request.path
        #home,property,blog

        if "property" in request.path:
            MostViewPage.objects.create(
                    name="PROPERTIES"
                )
        if "blog" in request.path:
            MostViewPage.objects.create(
                    name="BLOG"
                )
        if "home" in request.path:
            MostViewPage.objects.create(
                    name="HOME"
                )


            # Code to be executed for each request/response after
        # the view is called.
        return response