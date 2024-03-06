from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'message': 'Welcome to the Test API boilerplate',
        'version': '0.1',
        'author': 'Paulo Arbeláez',
        'Release': '20240306.16.21',
    })
