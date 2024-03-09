from django.contrib import admin
from django.urls import path, include
from .views import root_route
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route, name='root'),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls')
    ),

    # JWT Token Authentication
    path('dj-rest-auth/token/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path('dj-rest-auth/token/refresh/',
        TokenRefreshView.as_view(), name='token_refresh'
    ),
]
