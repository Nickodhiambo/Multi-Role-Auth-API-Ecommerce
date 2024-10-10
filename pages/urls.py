from django.urls import path

from .views import SignUpHome

urlpatterns = [
    path('api/v1/', SignUpHome.as_view(), name='home'),
]