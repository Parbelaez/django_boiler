from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import root_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route, name='root'),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
    path('accounts/', include('allauth.urls')),
]
