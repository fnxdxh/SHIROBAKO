from django.test import TestCase
from django.test.client import Client
import unittest
from hashlib import md5
from django.core.management import call_command
from website.models import *
import json
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


class TestCreateCompetition(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user(username="org2", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)

    def test_create_competition(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org2', 'password': '2018'})
        response = c.post('/api/create_competition/',{'name':'test','desc':'test','date1':'2018-12-25','date2':'2018-12-25','date3':'2018-12-26','date4':'2018-12-26','sponsor':'test'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

class TestIndexCompetitionList(unittest.TestCase):
    def setUp(self):
        Competition.objects.create(title='test1', description='test1', sign_up_end='2018-12-25', sign_up_start='2018-12-25', start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer1', sponsor='sponsor1')
        Competition.objects.create(title='test2', description='test2', sign_up_end='2018-12-25', sign_up_start='2018-12-25', start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer2', sponsor='sponsor2')
        Competition.objects.create(title='test3', description='test3', sign_up_end='2018-12-25', sign_up_start='2018-12-25', start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer3', sponsor='sponsor3')
    def test_index_competition_list(self):
        c = Client()
        response = c.get('/api/index_competition_list/')
        response = json.loads(response)
        print(response)

