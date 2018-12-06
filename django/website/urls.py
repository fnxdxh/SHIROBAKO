from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^register_competitor/', competitor_register),
]