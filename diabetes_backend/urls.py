
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from  rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_vew=get_schema_view(
    openapi.Info(
        title='Diabetes API',
        default_version='v1',
        description='API for daibetes app (profile, metrics,tips etc)',
        contact=openapi.Contact(email='nahabwesirmuel@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/jwt/create/',TokenObtainPairView.as_view(),name='jwt_create'),
    path('auth/jwt/refresh/',TokenRefreshView.as_view(),name='jwt_refresh'),
    path('auth/jwt/',include('djoser.urls.jwt')),


    path('swagger/',schema_vew.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_vew.with_ui('redoc',cache_timeout=0),name='schema-redoc')
]



#endpoints for djoser
# /auth/users/ - POST - Create a new user
# /auth/users/me/ - GET - Get the current user's details
# auth/jwt/create/
# /auth/jwt/refresh/ - POST - Refresh the JWT token
# /auth/users/me/
# /auth/jwt/logout



