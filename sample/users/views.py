from rest_framework import generics
from rest_auth.registration.views import RegisterView

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class CustomRegistrationView(RegisterView):

    def get_serializer_class(self):
        return serializers.CustomRegistrationSerializer
