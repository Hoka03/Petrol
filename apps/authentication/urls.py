from django.urls import path

from .views import RegisterSendCodeAPIView, RegisterAPIView, VerifyCodeAPIView, LoginAPIView, ChangePasswordAPIView

urlpatterns = [
    #   Register part
    path('register/send-code/', RegisterSendCodeAPIView.as_view(), name='register_send_code'),
    path('register/', RegisterAPIView.as_view(), name='register'),

    path('verify-code/', VerifyCodeAPIView.as_view(), name='verify_code'),

    #   Login part
    path('login/', LoginAPIView.as_view(), name='login'),

    #   Change password part
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password')
]

