from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^register_competitor/', competitor_register),
    url(r'^register_organizer/', organizer_register),
    url(r'^register_jury/', jury_register),
    url(r'^login_competitor/', competitor_login),
    url(r'^login_organizer/', organizer_login),
    url(r'^login_jury/', jury_login),
    url(r'^index_competition_list/', index_competition_list),
]