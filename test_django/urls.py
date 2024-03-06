from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import root_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route, name='root'),
    path('api-auth/', include('rest_framework.urls')),
]
