from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from users.views import CustomRegistrationView
from drvrequest.views import BookingViewSet


router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet, base_name='Booking')

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    url(r'^rest-auth/register/create/$', CustomRegistrationView.as_view(), name='custom-register'),

    url(r'', include(router.urls)),
]
