from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    user_type = models.IntegerField(choices=((0, 'CUSTOMER'), (1, 'DRIVER')), default=0)

    def __str__(self):
        return self.email
