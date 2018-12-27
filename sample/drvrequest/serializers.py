from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    customer = PrimaryKeyRelatedField(read_only=True)
    driver = PrimaryKeyRelatedField(read_only=True)
    status = serializers.IntegerField(default=0)

    class Meta:
        model = Booking
        fields = ('id', 'customer', 'driver', 'status')
