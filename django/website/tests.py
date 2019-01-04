from django.test import TestCase
from django.test.client import Client
import unittest
from hashlib import md5
import datetime
from django.core.management import call_command
from website.models import *
import json
from django.utils import timezone
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
        now_time = datetime.datetime.now(tz=timezone.utc)
        response = c.post('/api/login_organizer/', {'username': 'org2', 'password': '2018'})
        response = c.post('/api/create_competition/',{'title':'test','description':'test','sign_up_start':now_time+datetime.timedelta(days=8),'sign_up_end':now_time+datetime.timedelta(days=9),'start_time':now_time+datetime.timedelta(days=9),'end_time':now_time+datetime.timedelta(days=10),'sponsor':'test'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')


class TestOrganizerCompetitionList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="org_list", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,competition_list="test_list1,test_list2",status=Organizer.STATUS_CONFIRMED)
    def test_organizer_competition_list(self):
        c = Client()
        response = c.post('/api/login_organizer/', {'username': 'org_list', 'password': '2018'})
        response = c.get('/api/organizer_competition_list/')
        self.assertEqual(response.content.decode('utf-8'), '[{"title": "test_list1", "msg": "success", "error_num": 0}, {"title": "test_list2", "msg": "success", "error_num": 0}]')

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


class TestJuryCompetitionList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="jury_list", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user,competition_list="test_list1,test_list2")
    def test_jury_competition_list(self):
        c = Client()
        c.post('/api/login_jury/', {'username': 'jury_list', 'password': '2018'})
        response = c.get('/api/jury_competition_list/')
        self.assertEqual(response.content.decode('utf-8'), '[{"title": "test_list1", "msg": "success", "error_num": 0}, {"title": "test_list2", "msg": "success", "error_num": 0}]')



class TestIndexCompetitionList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        now_time = datetime.datetime.now(tz=timezone.utc)
        Competition.objects.create(title='test1', description='test1', sign_up_end=now_time, sign_up_start=now_time, start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer1', sponsor='sponsor1')
        Competition.objects.create(title='test2', description='test2', sign_up_end=now_time, sign_up_start=now_time, start_time='2018-12-26', end_time='2018-12-26',
                                                        organizer='organizer2', sponsor='sponsor2')
    
    def test_index_competition_list(self):
        c = Client()
        response = c.get('/api/index_competition_list/')
        response = json.loads(response.content)
        print(response)


class TestUploadFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        now_time = datetime.datetime.now(tz=timezone.utc)
        user = User.objects.create_user(username="comp1", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)
        Competition.objects.create(title='test_upload', description='test_upload', sign_up_end=now_time+datetime.timedelta(days=7), sign_up_start=now_time, start_time=now_time, end_time=now_time + datetime.timedelta(days=7),
                                                        organizer='org4', sponsor='sponsor5')
    def test_upload_file(self):
        c = Client()
        c.post('/api/login_competitor/',{'username':'comp1','password':'2018'})
        with open('test.txt','rb') as fp:
            response = c.post('/api/upload/', {'userfile':fp,'competition':'test_upload'})
            content = json.loads(response.content)
            self.assertEqual(content['msg'], "success")



class TestDividePaper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        now_time = datetime.datetime.now(tz=timezone.utc)
        user = User.objects.create_user(username="jury2", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
        user = User.objects.create_user(username="jury3", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
        user = User.objects.create_user(username="org4", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Org")
        Organizer.objects.create(user=user,status=Organizer.STATUS_CONFIRMED)
        Competition.objects.create(title='test4', description='test4', sign_up_end=now_time+ datetime.timedelta(days=1), sign_up_start=now_time , start_time=now_time, end_time=now_time + datetime.timedelta(days=1),
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
        self.assertEqual(response.content.decode('utf-8'),'{"msg": "success", "error_num": 0}')


class TestGradeUpload(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        UserFile.objects.create(username="test",competition="test_grade",file_url="test_grade.txt",grade_list="0",jury_list='jury_grade',jury_count=1)
        user = User.objects.create_user(username="jury_grade", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Rat")
        Jury.objects.create(user=user)
    def test_upload_grade(self):
        c = Client()
        response = c.post('/api/login_jury/', {'username': 'jury_grade', 'password': '2018'})
        response = c.post('/api/grade_upload/',{'grade':'98','filepath':'test_grade.txt'})
        self.assertEqual(response.content.decode('utf-8'),'{"msg": "success", "error_num": 0}')

class TestCompetitorSignUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        now_time = datetime.datetime.now(tz=timezone.utc)
        user = User.objects.create_user(username="comp5", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)
        Competition.objects.create(title='test_sign_up', description='test_sign_up', sign_up_end=now_time+datetime.timedelta(days=7), sign_up_start=now_time, start_time=now_time, end_time=now_time + datetime.timedelta(days=7),
                                                        organizer='org4', sponsor='sponsor5')
        Competition.objects.create(title='test_sign_up_list', description='test_sign_up_list', sign_up_end=now_time+datetime.timedelta(days=7), sign_up_start=now_time, start_time=now_time, end_time=now_time + datetime.timedelta(days=7),
                                                        organizer='org4', sponsor='sponsor5')
        Competition.objects.create(title='test_sign_up_out', description='testouttime', sign_up_end=now_time-datetime.timedelta(days=8), sign_up_start=now_time-datetime.timedelta(days=9), start_time=now_time, end_time=now_time + datetime.timedelta(days=7),
                                                        organizer='org4', sponsor='sponsor5')

    def test_competitor_sign_up(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp5','password':'2018'})
        #print(response.content)
        response = c.get('/api/sign_up/',{'competition_name':'test_sign_up'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "success", "error_num": 0}')

    def test_competitor_sign_up_again(self):
        c = Client()
        c.post('/api/login_competitor/',{'username':'comp5','password':'2018'})
        #print(response.content)
        c.get('/api/sign_up/',{'competition_name':'test5'})
        response = c.get('/api/sign_up/',{'competition_name':'test_sign_up'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "signed up", "error_num": 1}')

    def test_competitor_sign_up_out_of_time(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp5','password':'2018'})
        #print(response.content)
        response = c.get('/api/sign_up/',{'competition_name':'test_sign_up_out'})
        self.assertEqual(response.content.decode('utf-8'), '{"msg": "out of time", "error_num": 1}')

    def test_competitor_competition_list(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp5','password':'2018'})
        #print(response.content)
        response = c.get('/api/sign_up/',{'competition_name':'test_sign_up_list'})
        response = c.get('/api/competitor_competition_list/')
        self.assertEqual(response.content.decode('utf-8'), '[{"title": "test_sign_up_list", "msg": "success", "error_num": 0}]')

class TestCompetitorCompetitionList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username="comp_test", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user, competition_list='test_test')
        user = User.objects.create_user(username="comp_test_null", password=md5(("2018").encode('utf-8')).hexdigest(), user_type="Comp")
        Competitor.objects.create(user=user)

    def test_competitor_competition_list(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp_test','password':'2018'})
        response = c.get('/api/competitor_competition_list/')
        self.assertEqual(response.content.decode('utf-8'), '[{"title": "test_test", "msg": "success", "error_num": 0}]')

    def test_competitor_competition_list_null(self):
        c = Client()
        response = c.post('/api/login_competitor/',{'username':'comp_test_null','password':'2018'})
        response = c.get('/api/competitor_competition_list/')
        self.assertEqual(response.content.decode('utf-8'), '[{"msg": "no competition", "error_num": 1}]')

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