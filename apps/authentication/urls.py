from django.urls import path

from apps.authentication.views import SendAuthCodeAPIView

urlpatterns = [
    path('code/', SendAuthCodeAPIView.as_view(), name='send_code')
]