from django.test import TestCase
from django.test.client import Client
import unittest
from django.core.management import call_command
from website.models import *
# Create your tests here.


class TestRegister(unittest.TestCase):
    def setUpTestData(self):
        user = User.objects.create(username="comp", password="1b3d0dcbbe36bbb35e3820ead8856fbb", salt='mHTT')
        #user = User.objects.create(username="goood", password="1b3d0dcbbe36bbb35e3820ead8856fbb", salt="mHTT")
        Competitor.objects.create(user=user, uniq_id=0o012, competition_list="hello")
        call_command('loaddata', 'myfixture', verbosity=0)

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
        response = c.post('/api/register_jury/', {'username': 'jury', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_competitor_login(self):
        c = Client()
        response = c.post('/api/login_competitor/', {'username': 'comp', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    #def test_organizer_login(self):
        #c = Client()
        #response = c.post('/api/login_organizer/', {'username': 'organizer', 'password': '2018'})
        #self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    #def test_jury_login(self):
       # c = Client()
       # response = c.post('/api/login_jury/', {'username': 'jury', 'password': '2018'})
        #elf.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')



