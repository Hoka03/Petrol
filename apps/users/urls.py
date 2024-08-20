from django.urls import path

from .views import CustomUserRetrieveUpdateAPIView

urlpatterns = [
    path('', CustomUserRetrieveUpdateAPIView.as_view(), name='user_list')
]