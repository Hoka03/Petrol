from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.complaints.models import Complaint
from apps.complaints.serializers import ComplaintCreateSerializer


class ComplaintCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ComplaintCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ComplaintListCreateGenericAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Complaint.objects.all()
    serializer_class = ComplaintCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['salom'] = 100
        return context


class ComplainUpdateDeleteGenericAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Complaint.objects.all()
    serializer_class = ComplaintCreateSerializer
