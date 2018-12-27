from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'driver', 'status')
    list_filter = ('status', )


admin.site.register(Booking, BookingAdmin)
