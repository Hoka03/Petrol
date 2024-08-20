from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__', include("debug_toolbar.urls")),
    #   APPS OF VIEWS
    path('api/v1/auth/', include('apps.authentication.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/bookings/', include('apps.booking.urls')),
    path('api/v1/complaints/', include('apps.complaints.urls')),
    path('api/v1/cars/', include('apps.cars.urls')),
    #   SWAGGER
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
