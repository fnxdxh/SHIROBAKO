from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^register_competitor/', competitor_register),
    url(r'^register_organizer/', organizer_register),
    url(r'^register_jury/', jury_register),
    url(r'^login_competitor/', competitor_login),
    url(r'^login_organizer/', organizer_login),
    url(r'^login_jury/', jury_login),
    url(r'^login_superuser/', admin_login),
    url(r'^index_competition_list/', index_competition_list),
    url(r'^jury_competition_list/', jury_competition_list),
    url(r'^organizer_competition_list/', organizer_competition_list),
    url(r'^upload/', file_upload),
    url(r'^file_download/', file_download),
    url(r'^create_competition/',create_competition),
    url(r'^wait_list/', admin_to_confirm_list),
    url(r'^recognize/', admin_to_confirm),
    url(r'^upload_grade/', grade_upload),
    url(r'^competition_detail/', competition_detail),
    url(r'^sign_up/', competitor_sign_up),
    url(r'^divide_paper/', divide_paper),
    url(r'^file_list/', file_list),
    url(r'^invite_jury/', invite_jury),
    url(r'^sign_up/', competitor_sign_up),
    url(r'^grade_upload/', grade_upload),
]