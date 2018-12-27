from django.db import models
from users.models import CustomUser

# Create your models here.


class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    driver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='booking_driver')
    status = models.IntegerField(choices=((0, 'NEW'), (1, 'ACCEPTED'), (2, 'REJECTED')), default=0)

    def __str__(self):
        return 'Booking from #{}'.format(self.customer.username)
