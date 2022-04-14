from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Pizza Delivery API",
        default_version='v1',
        description="A REST API for a Pizza delivery service",
        contact=openapi.Contact(email="admin@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger<format>.json|.yaml',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
