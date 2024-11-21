from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Techinal test",
      default_version='v1',
      description="API REST WITH DATABASES",
      terms_of_service="https://www.django-rest-framework.org",
      contact=openapi.Contact(email="alvarojavieralvarezperez@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('docstest/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  
]
