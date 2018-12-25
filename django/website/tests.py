from django.test import TestCase
from django.test.client import Client
import unittest
from hashlib import md5
from django.core.management import call_command
from website.models import *
# Create your tests here.


class TestRegister(unittest.TestCase):
    '''def setUp(self):
        user = User.objects.create_user(username="comp", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        user = User.objects.create(username="goood", password="1b3d0dcbbe36bbb35e3820ead8856fbb", salt="mHTT")
        Competitor.objects.create(user=user)
        user = User.objects.create_user(username="org", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_UNCONFIRM)
        user = User.objects.create_user(username="jury", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
        call_command('loaddata', 'myfixture', verbosity=0)'''

    def test_competitor_register(self):
        c = Client()
        response = c.post('/api/register_competitor/', {'username': 'competitor', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_organizer_register(self):
        c = Client()
        response = c.post('/api/register_organizer/', {'username': 'organizer', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_jury_register(self):
        c = Client()
        response = c.post('/api/register_jury/', {'username': 'myjury', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

class TestCompetitorLogin(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user(username="comp", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        #user = User.objects.create(username="goood", password="1b3d0dcbbe36bbb35e3820ead8856fbb", salt="mHTT")
        Competitor.objects.create(user=user)
        #user = User.objects.create_user(username="org3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        #Organizer.objects.create(user=user,status=Organizer.STATUS_UNCONFIRM,competition_list="")
        #user = User.objects.create_user(username="jury3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        #Jury.objects.create(user=user,competition_list="")

    def test_competitor_login(self):
        c = Client()
        response = c.post('/api/login_competitor/', {'username': 'comp', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')


class TestJuryLogin(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user(username="jury", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)

    def test_jury_login(self):
        c = Client()
        response = c.post('/api/login_jury/', {'username': 'jury', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

class TestOrganizerLogin(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user(username="org", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_UNCONFIRM)

        user = User.objects.create_user(username="org1", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)
        #user = User.objects.create_user(username="jury3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        #Jury.objects.create(user=user,competition_list="")
    def test_organizer_login(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "have not confirmed", "error_num": 1}')
        response = c.post('/api/login_organizer/', {'username': 'org1', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')





