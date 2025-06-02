from django.urls import path
from .views import pong

app_name = "api"

urlpatterns = [
    path("ping/", pong, name="pong"),
]
