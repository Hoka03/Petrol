from django.urls import path

from apps.complaints import views


urlpatterns = [
    path('', views.ComplaintCreateAPIView.as_view(), name='complaint_create'),
    path('generics/', views.ComplaintListCreateGenericAPIView.as_view(),
         name='complaint_generic_create'),
    path('generics/<int:pk>/', views.ComplainUpdateDeleteGenericAPIView.as_view(),
         name='complaint_generic_update_delete'),
]
