from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('reg', views.CustomRegistrationView.as_view()),
]
