from django.contrib.auth import get_user_model
from drf_yasg.openapi import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import CustomUserSerializer


class CustomUserRetrieveUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)