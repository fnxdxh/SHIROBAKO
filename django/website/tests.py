from django.test import TestCase
from django.test.client import Client
import unittest
from hashlib import md5
import datetime
from django.core.management import call_command
from website.models import *
import json
# Create your tests here.


class TestRegister(unittest.TestCase):

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
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="comp", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)

    def test_competitor_login(self):
        c = Client()
        response = c.post('/api/login_competitor/', {'username': 'comp', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_competitor_login1(self):
        c = Client()
        response = c.post('/api/login_competitor/', {'username': 'comp'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "input error", "error_num": 1}')

    def test_competitor_login2(self):
        c = Client()
        response = c.post('/api/login_competitor/', {'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "input error", "error_num": 1}')

class TestJuryLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="jury", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)

    def test_jury_login(self):
        c = Client()
        response = c.post('/api/login_jury/', {'username': 'jury', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_jury_login1(self):
        c = Client()
        response = c.post('/api/login_jury/', {'username': 'jury'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "input error", "error_num": 1}')

    def test_jury_login2(self):
        c = Client()
        response = c.post('/api/login_jury/', {'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "input error", "error_num": 1}')

class TestAdminLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_superuser(username="superuser",email="", password='2018', user_type="SU")

    def test_admin_login(self):
        c = Client()
        response = c.post('/api/login_superuser/', {'username': 'superuser', 'password':'2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')



class TestOrganizerLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="org", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_UNCONFIRM)

        user = User.objects.create_user(username="org1", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)

    def test_organizer_login_unconfirm(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "have not confirmed", "error_num": 1}')

    def test_organizer_login_confirmed(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org1', 'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_organizer_login_confirmed1(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org1'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "input error", "error_num": 1}')

    def test_organizer_login_confirmed2(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'password': '2018'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "input error", "error_num": 1}')

class TestCreateCompetition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="org2", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)

    def test_create_competition(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org2', 'password': '2018'})
        response = c.post('/api/create_competition/',{'title':'test','description':'test','sign_up_start':'2018-12-25','sign_up_end':'2018-12-25','start_time':'2018-12-26','end_time':'2018-12-26','sponsor':'test'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')


class TestCompetitorCompetitionList(unittest.TestCase):
    def test_competitor_competition_list(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org2', 'password': '2018'})


class TestInviteJury(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="jury1", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
        user = User.objects.create_user(username="org3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)
        Competition.objects.create(title='test3', description='test3', sign_up_end='2018-12-25', sign_up_start='2018-12-25', start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='org3', sponsor='sponsor3')
    def test_invite_jury(self):
        c = Client()
        c.post('/api/login_organizer/', {'username': 'org3', 'password': '2018'})
        response = c.post('/api/invite_jury/',{"jury":"jury1","competition_name":"test3"})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')


class TestIndexCompetitionList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        now_time = datetime.datetime.now()
        Competition.objects.create(title='test1', description='test1', sign_up_end=now_time, sign_up_start=now_time, start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer1', sponsor='sponsor1')
        Competition.objects.create(title='test2', description='test2', sign_up_end=now_time, sign_up_start=now_time, start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer2', sponsor='sponsor2')
    
    def test_index_competition_list(self):
        c = Client()
        response = c.get('/api/index_competition_list/')
        response = json.loads(response.content)
        print(response)
        self.assertEqual(response,[{'title': 'test1', 'sponsor': 'sponsor1','start_time': '2018-12-26', 'end_time': '2018-12-26', 'msg': 'success', 'error_num': 0}, 
                                   {'title': 'test2', 'sponsor': 'sponsor2','start_time': '2018-12-26', 'end_time': '2018-12-26', 'msg': 'success', 'error_num': 0}])



class TestUploadFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="comp1", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)

    def test_upload_file(self):
        c = Client()
        c.post('/api/login_competitor/',{'username':'comp1','password':'2018'})
        with open('test.txt','rb') as fp:
            response = c.post('/api/upload/', {'userfile':fp,'competition':'小程序竞赛'})
            content = json.loads(response.content)
            self.assertEqual(content['msg'], "success")



class TestDividePaper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="jury2", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
        user = User.objects.create_user(username="jury3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
        user = User.objects.create_user(username="org4", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)
        Competition.objects.create(title='test4', description='test4', sign_up_end='2018-12-25', sign_up_start='2018-12-25', start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='org4', sponsor='sponsor4')
        user = User.objects.create_user(username="comp2", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)
        user = User.objects.create_user(username="comp3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)
        user = User.objects.create_user(username="comp4", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)

    def test_divide_paper(self):
        c = Client()
        c.post('/api/login_competitor/',{'username':'comp2','password':'2018'})
        response = c.get('/api/sign_up/',{'competition_name':'test4'})
        #print(response.content)
        with open('test1.txt','rb') as fp:
            response = c.post('/api/upload/', {'userfile':fp,'competition':'test4'})
            #print(response.content)
        c.post('/api/login_competitor/',{'username':'comp3','password':'2018'})
        c.get('/api/sign_up/',{'competition_name':'test4'})
        with open('test2.txt','rb') as fp:
            response = c.post('/api/upload/', {'userfile':fp,'competition':'test4'})
            #print(response.content)
        c.post('/api/login_competitor/',{'username':'comp4','password':'2018'})
        c.get('/api/sign_up/',{'competition_name':'test4'})
        with open('test3.txt','rb') as fp:
            response = c.post('/api/upload/', {'userfile':fp,'competition':'test4'})
            #print(response.content)
        c.post('/api/login_organizer/', {'username': 'org4', 'password': '2018'})
        response = c.post('/api/invite_jury/',{"jury":"jury2","competition_name":"test4"})
        #print(response.content)
        response = c.post('/api/invite_jury/',{"jury":"jury3","competition_name":"test4"})
        #print(response.content)
        response = c.post('/api/divide_paper/',{'competition_name':'test4','time':2})
        #print(response.content)
        response = c.post('/api/login_jury/', {'username': 'jury2', 'password': '2018'})
        response = c.post('/api/grade_upload/',{'grade':'98','filepath':'test2.txt'})
        #print(response.content)

class TestCompetitorSignUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="comp5", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)
        Competition.objects.create(title='test5', description='test5', sign_up_end='2018-12-25', sign_up_start='2018-12-25', start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='org4', sponsor='sponsor5')
    def test_competitor_sign_up(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp5','password':'2018'})
        response = c.get('/api/sign_up/',{'competition_name':'test5'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

class TestCheckGrade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="comp6", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)
        UserFile.objects.create(username='comp6',competition='test_test_grade',grade=98.8)
        UserFile.objects.create(username='comp6',competition='test_grade_list',grade_list="100,98,99",jury_count=3)

    def test_check_grade(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp6','password':'2018'})
        response = c.get('/api/check_grade/',{'competition_name':'test_test_grade'})
        self.assertEqual(response.content.decode('utf-8'), '{"grade": 98.8, "msg": "success", "error_num": 0}')
    
    def test_grade_list(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp6','password':'2018'})
        response = c.get('/api/check_grade/',{'competition_name':'test_grade_list'})
        self.assertEqual(response.content.decode('utf-8'), '{"grade": 99.0, "msg": "success", "error_num": 0}')