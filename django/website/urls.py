from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^register_competitor/', competitor_register),
    url(r'^getList/', index_competition_list),
]