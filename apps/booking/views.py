from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingCreateSerializer
from .permissions import CheckUserBalance


class BookingCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, CheckUserBalance)

    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
