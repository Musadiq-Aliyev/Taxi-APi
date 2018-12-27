from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer


# Create your views here.
class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.user_type == 0:
            return Booking.objects.filter(customer=self.request.user)
        else:
            return Booking.objects.filter(status=0)

    def perform_create(self, serializer):
        instance = serializer.save(customer=self.request.user)
        return super(BookingViewSet, self).perform_create(serializer)
