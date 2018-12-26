from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from datetime import datetime
from django.utils import timezone
from hashlib import md5
from random import Random
from mysite import settings
from django.contrib import auth
import os
import uuid
import json
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User, Competitor, Organizer, Jury, Competition, UserFile, SuperUser, JuryFile
# Create your views here.


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    # 获取chars的最大下标
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次随机从chars中抽取一位，拼接成一个salt值
        salt += chars[random.randint(0, len_chars)]
    return salt


# 获取原始密码+salt的md5值
def create_md5(pwd):
    md5_obj = md5()
    md5_obj.update(pwd.encode('utf-8'))
    return md5_obj.hexdigest()


def competitor_register(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if username and password:
            try:
                #salt = create_salt()
                md5_pwd = create_md5(password)
                uniq = uuid.uuid5(uuid.NAMESPACE_DNS, username)
                print(md5_pwd)
                print(username)
                user = User.objects.create_user(username=username, password=md5_pwd, unique_id=uniq, user_type='Comp')
                Competitor.objects.create(user=user)
                response['msg'] = 'success'
                response['error_num'] = 0
            except:
                response['msg'] = 'create failed'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'have no data'
    response['error_num'] = 1
    return JsonResponse(response)


def jury_register(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                #salt = create_salt()
                md5_pwd = create_md5(password)
                uniq = uuid.uuid5(uuid.NAMESPACE_DNS, username)
                print(md5_pwd)
                print(username)
                user = User.objects.create_user(username=username, password=md5_pwd, unique_id=uniq, user_type='Rat')
                Jury.objects.create(user=user, tel="18853505212")
                response['msg'] = 'success'
                response['error_num'] = 0
            except:
                response['msg'] = 'create failed'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'have no data'
    response['error_num'] = 1
    return JsonResponse(response)


def organizer_register(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                #salt = create_salt()
                md5_pwd = create_md5(password)
                uniq = uuid.uuid5(uuid.NAMESPACE_DNS, username)
                user = User.objects.create_user(username=username, password=md5_pwd, unique_id=uniq, user_type='Org')
                Organizer.objects.create(user=user, status=Organizer.STATUS_UNCONFIRM)
                response['msg'] = 'success'
                response['error_num'] = 0
            except:
                response['msg'] = 'create failed'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'have no data'
    response['error_num'] = 1
    return JsonResponse(response)


def competitor_login(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            try:
                #user = User.objects.find(username=username)
                #salt = user.salt
                pwd = create_md5(password)
                #if pwd == user.password:
                print(pwd)
                print(username)
                user = authenticate(username=username, password=pwd)
                #user = User.objects.find(username=username, password=pwd)
                if user.user_type == "Comp":
                    login(request, user)
                    request.session['username'] = username
                    request.session.set_expiry(600)  #设置session的过期时间，为600s
                    response['msg'] = 'success'
                    response['error_num'] = 0
                else:
                    response['msg'] = 'no permission'
                    response['error_num'] = 1
            except:
                response['msg'] = 'find failed'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'create failed'
    response['error_num'] = 1
    return JsonResponse(response)


def jury_login(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            try:
                pwd = create_md5(password)
                user = authenticate(username=username, password=pwd)
                if user.user_type == "Rat":
                    login(request, user)
                    request.session['username'] = username
                    request.session.set_expiry(600)  #设置session的过期时间，为600s
                    response['msg'] = 'success'
                    response['error_num'] = 0
                else:
                    response['msg'] = 'no permission'
                    response['error_num'] = 1
            except:
                response['msg'] = 'no user'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'create failed'
    response['error_num'] = 1
    return JsonResponse(response)

def organizer_login(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            pwd = create_md5(password)
            #user = authenticate(username=username, password=pwd)
            try:
                user = authenticate(username=username, password=pwd)
            #if user is not None and (user.user_type == "Org"):
                print(user.organizer.status)
                if user.organizer.status == Organizer.STATUS_CONFIRMED:
                    login(request, user)
                    response['msg'] = 'success'
                    response['error_num'] = 0
                elif user.organizer.status == Organizer.STATUS_UNCONFIRM:
                    response['msg'] = 'have not confirmed'
                    response['error_num'] = 1
            except:
                response['msg'] = 'failed'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'failed'
    response['error_num'] = 1
    return JsonResponse(response)



def admin_login(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    response['msg'] = 'success'
                    response['error_num'] = 0
                else:
                    response['msg'] = 'create failed'
                    response['error_num'] = 1
                return JsonResponse(response)
    response['msg'] = 'create failed'
    response['error_num'] = 1
    return JsonResponse(response)


def index_competition_list(request):
    now_time = timezone.now()
    competition_list = Competition.objects.filter(Q(sign_up_start__gte=now_time) | Q(sign_up_end__lt=now_time))
    response = []
    if competition_list is not None:
        for competition in competition_list:
            cmp = {}
            cmp['title'] = competition.title
            cmp['organizer'] = competition.organizer
            cmp['type'] = competition.type
            start_time_list = competition.start_time.split(',')
            cmp['start_time'] = start_time_list[0]
            end_time_list = competition.end_time.split(',')
            cmp['end_time'] = end_time_list[-1]
            cmp['msg'] = 'success'
            cmp['error_num'] = 0
            response.append(cmp)
            print(response)
        return HttpResponse(json.dumps(response))
    cmp = {}
    cmp['msg'] = 'no data failed'
    cmp['error_num'] = 1
    response.append(cmp)
    print(json.dumps(response))
    print(cmp)
    return HttpResponse(json.dumps(response))


def competitor_competition_list(request):
    response = []
    fail_msg = {}
    if request.user.is_authenticated():
        try:
            #competitor = Competitor.objects.find(user=request.user)
            competitor = request.user.competitor
            competition_list = competitor.activity_list.split(',')
            if competition_list is not None:
                for title in competition_list:
                    org = {}
                    org['title'] = title
                    org['msg'] = 'success'
                    org['error_num'] = 0
                    response.append(org)
                return JsonResponse(json.dumps(response))
            fail_msg['msg'] = 'no competition'
            fail_msg['error_num'] = 1
            response.append(fail_msg)
            return JsonResponse(json.dumps(response))
        except:
            fail_msg['msg'] = 'failed'
            fail_msg['error_num'] = 1
    fail_msg['msg'] = 'no user'
    fail_msg['error_num'] = 1
    response.append(fail_msg)
    return JsonResponse(json.dumps(response))


def jury_competition_list(request):
    response = []
    fail_msg = {}
    if request.user.is_authenticated():
        try:
            #jury = jury.objects.find(user=request.user)
            jury = request.user.jury
            competition_list = jury.activity_list.split(',')
            if competition_list is not None:
                for title in competition_list:
                    org = {}
                    org['title'] = title
                    org['msg'] = 'success'
                    org['error_num'] = 0
                    response.append(org)
                    
                return JsonResponse(response)
            fail_msg['msg'] = 'recent has no competition'
            fail_msg['error_num'] = 1
            response.append(fail_msg)
            return JsonResponse(response)
        except:
            fail_msg['msg'] = 'failed'
            fail_msg['error_num'] = 1
    fail_msg['msg'] = 'failed'
    fail_msg['error_num'] = 1
    response.append(fail_msg)
    return JsonResponse(response)


def organizer_competition_list(request):
    response = []
    fail_msg = {}
    if request.user.is_authenticated():
        try:
            #organizer = Competitor.objects.find(user=request.user)
            organizer = request.user.organizer
            competition_list = organizer.activity_list.split(',')
            if competition_list is not None:
                for title in competition_list:
                    org = {}
                    org['title'] = title
                    org['msg'] = 'success'
                    org['error_num'] = 0
                    response.append(org)
                return JsonResponse(response)
            fail_msg['msg'] = 'recent has no competition'
            fail_msg['error_num'] = 1
            response.append(fail_msg)
            return JsonResponse(response)
        except:
            fail_msg['msg'] = 'failed'
            fail_msg['error_num'] = 1
    fail_msg['msg'] = 'failed'
    fail_msg['error_num'] = 1
    response.append(fail_msg)
    return JsonResponse(response)


def competitor_sign_up(request):
    response = {}
    if request.user.is_authenticated():
        competitor = request.user.competitor
        if request.method == "GET":
            name = request.GET.get("competition_name")
            try:
                competition = Competition.objects.find(title=name)
                if competitor.competition_list is not None:
                    competitor.competition_list = competition.competition_list + "," + name
                else:
                    competition.competitor_list = str(competitor.uniq_id)
                competitor.save()
                if competition.competitor_list is not None:
                    competitor.competition_list = competitor.competition_list + "," + str(competitor.uniq_id)
                else:
                    competitor.competition_list = name
                competitor.save()
                response['msg'] = 'success'
                response['error_num'] = 0
                return JsonResponse(response)
            except:
                response['msg'] = 'failed'
                response['error_num'] = 1
                return JsonResponse(response)
    response['msg'] = 'not login'
    response['error_num'] = 1
    return JsonResponse(response)


# 参考：https://www.jianshu.com/p/1a5546ce0c92
def file_upload(request):
    response = {}
    print("ok")
    print(request.user)
    if request.user.is_authenticated():
        print("ok")
        if request.method == "POST":
            #competition = request.POST.get("competition")
            file = request.FILES.get("userfile", None)
            competition = request.POST.get('competition')
            name = file.name.split('.')
            file_name = name[0] + request.user.unique_id[0:10] + '.'+name[-1] 
            print(file_name)
            with open('templates/file/%s' % file_name, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            print("ok")
            file_url = os.path.join('/file', file_name).replace('\\', '/')
            url = "http://" + settings.SITE_DOMAIN + file_url
            #competitor = request.user.competitor
            try:
                file = UserFile.objects.find(username=request.user.username, competition=competition)
                file.file_url = url
                file.save()
                response['msg'] = 'success'
                response['error_num'] = 0
                return JsonResponse(response)
            except:
                UserFile.objects.create(username=request.user.username, competition=competition, file_url=url)
                response['msg'] = 'success'
                response['error_num'] = 0
                return JsonResponse(response)
    response['msg'] = 'not login'
    response['error_num'] = 1
    return JsonResponse(response)


# 参考网址：https://blog.igevin.info/posts/django-download-function/
#           https://blog.csdn.net/qq_30291335/article/details/79497911
def file_download(request):
    if request.method == "POST":
        file = request.POST.get('file')
        try:
            def file_iterator(file_name, chunk_size=512):
                with open(file_name) as f:
                    while True:
                        c = f.read(chunk_size)
                        if c:
                            yield c
                        else:
                            break
            #filename = "test.txt"
            response = StreamingHttpResponse(file_iterator(file))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
            return response
        except:
            return HttpResponse("download failed")
    return HttpResponse("method wrong")


def grade_upload(request):
    response = {}
    if request.user.is_authenticated():
        if request.method == "POST":
            grade = request.POST.get("grade")
            file_url = request.POST.get("filepath")
            try:
                file = UserFile.objects.find(file_url=file_url)
                grade = file.grade_list.split(',')
                jury_list=file.jury_list.split(',')
                i = 0
                for jury in jury_list:
                    if jury == request.user.username:
                        grade[i] = grade
                str = ','
                file.grade_list = str.join(grade)
                file.save()
                response['msg'] = 'success'
                response['error_num'] = 0
                return JsonResponse(response)
            except:
                response['msg'] = 'failed'
                response['error_num'] = 1
                return JsonResponse(response)
    response['msg'] = 'not login'
    response['error_num'] = 1
    return JsonResponse(response)


def file_list(request):
    response = []
    org = {}
    if request.user.is_authenticated():
        if request.method == "POST":
            competition = request.POST.get("competition_name")
            try:
                jury_file = JuryFile.objects.find(competition=competition, jury=request.user.username)
                file_list = jury_file.file_list.split(",")
                for file in file_list:
                    org['name'] = file
                    org['msg'] = 'success'
                    org['error_num'] = 0
                    response.append(org)
                return JsonResponse(response)
            except:
                org['msg'] = 'failed'
                org['error_num'] = 1
                response.append(org)
                return JsonResponse(response)
    org['msg'] = 'not login'
    org['error_num'] = 0
    response.append(org)
    return JsonResponse(response)


def competition_detail(request):
    response = []
    detail = {}
    if request.method == "POST":
        activity_name = request.POST.get("competition_title")
        try:
            activity = Competition.objects.find(title=activity_name)
            detail['title'] = activity.title
            detail['stage'] = activity.stage
            detail['organizor'] = activity.organizor.name
            detail['description'] = activity.description
            detail['msg'] = 'success'
            detail['error_num'] = 0
            response.append(detail)
            return JsonResponse(response)
        except:
            detail['msg'] = 'failed'
            detail['error_num'] = 1
            response.append(detail)
            return JsonResponse(response)
    detail['msg'] = 'failed'
    detail['error_num'] = 1
    response.append(detail)
    return JsonResponse(response)


def admin_to_confirm_list(request):
    organizer_list = []
    org = {}
    if request.user.is_superuser:
        organizers = Organizer.objects.filter(status=Organizer.STATUS_UNCONFIRM)
        if organizers is not None:
            for organizer in organizers:
                org['username'] = organizer.username
                org['msg'] = 'success'
                org['error_num'] = 0
                organizer_list.append(org)
            return JsonResponse(organizer_list)
        org['msg'] = 'no'
        org['error_num'] = 0
        organizer_list.append(org)
        return JsonResponse(json.dumps(organizer_list))
    org['msg'] = 'failed'
    org['error_num'] = 1
    organizer_list.append(org)
    return JsonResponse(json.dumps(organizer_list))


def admin_to_confirm(request):
    response = {}
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            organizer = Organizer.objects.find(username=username, status=Organizer.STATUS_UNCONFIRM)
            organizer.status = Organizer.STATUS_CONFIRMED
            organizer.save()
            response['msg'] = 'success'
            response['error_num'] = 0
            return JsonResponse(response)
        except:
            response['msg'] = 'failed'
            response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'failed'
    response['error_num'] = 1
    return JsonResponse(response)

# 把paper_count张卷子平均划分为per_person个任务
def partition(Task,paper_count,per_person,file_list):
    for i in range(paper_count):
        Task[i/per_person][i%per_person] = file_list[i].file_url
        file_list[i].jury_count = file_list[i].jury_count + 1
        file_list[i].save()


#把第m个任务分给第K个阅卷人
def assign(Task,jury_li,m,k,per_person):
    for i in range(per_person):
        #Teacher[k][i] = Task[m][i]
        if jury_li[k].file_list is None:
            jury_li[k].file_list = Task[m][i].file_url
        else:
            jury_li[k].file_list = jury_li[k].file_list + "," + Task[m][i].file_url
        jury_li[k].file_count = jury_li[k].file_count + 1
        jury_li[k].save()
        if Task[m][i].jury_list is None:
            Task[m][i].jury_list = jury_li[k].jury
        else:
            Task[m][i].jury_list = Task[m][i].jury_list + "," + jury_li[k].jury
        if Task[m][i].grade_list is None:
            Task[m][i].grade_list = '0'
        else:
            Task[m][i].grade_list = Task[m][i].grade_list + ",0" 
        Task[m][i].jury_count = Task[m][i].jury_count + 1
        Task[m][i].save()


def divide_paper(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            title = request.POST.get("competition_name")
            per_time = int(request.POST.get("time")) #阅卷次数
            file_list=[]
            jury_li = []
            try:
                competition = Competition.objects.find(title=title, organizer=request.user.username)
                user_list = competition.competitor_list.split(",")
                paper_count = len(user_list)  #试卷数量
                jury_list = competition.jury_list.split(",")
                jury_count = len(jury_list)   #阅卷人数
                per_person = paper_count/jury_count + 1 #每个人平均任务量
                for user in user_list:
                    new_file = UserFile.objects.find(username=user, competition=title)
                    file_list.append(new_file)
                for jury in jury_list:
                    new_jury = JuryFile.objects.find(jury=jury, competition=title)
                    jury_li.append(new_jury)
                Task = [range(per_person) for i in range(jury_count)] 
                #Teacher = [(range(per_person) for i in range(jury_count)]
                partition(Task,paper_count,per_person,file_list)
                for i in range(per_time):
                    count = 0
                    j = i
                    for count in range(jury_count):
                        assign(Task,jury_li,count,j,per_person)
            except:
                return HttpResponse("divide fail")
        return HttpResponse("method wrong")
    return HttpResponse("not log in")


def create_competition(request):
    response = {}
    if request.user.is_authenticated() and request.user.user_type=='Org':
        if request.method == "POST":
            title = request.POST.get('name')
            description = request.POST.get('desc')
            sign_up_start = request.POST.get('date1')
            sign_up_end = request.POST.get('date2')
            start_time = request.POST.get('date3')
            end_time = request.POST.get("date4")
            sponsor = request.POST.get('sponsor')
            # there are some information of the competition
            organizer = request.user.username
            try:
                competiton = Competition.objects.create(title=title, description=description, sign_up_end=sign_up_end, sign_up_start=sign_up_start, start_time=start_time, end_time=end_time,
                                                        organizer=organizer, sponsor=sponsor)
                response['msg'] = 'success'
                response['error_num'] = 0
            except:
                response['msg'] = 'error'
                response['error_num'] = 1
            return JsonResponse(response)
    response['msg'] = 'failed'
    response['error_num'] = 1
    return JsonResponse(response)
    #response['msg'] = 'not log in'
    #response['error_num'] = 1
    #return JsonResponse(response)


def invite_jury(request):
    response = {}
    if request.user.is_authenticated():
        if request.method == "POST":
            jury = request.POST.get("jury")
            title = request.POST.get("competition_name")
            try:
                pre_jury = JuryFile.objects.filter(jury=jury, competition=title)
                if pre_jury is not None:
                    response['msg'] = 'exist'
                    response['error_num'] = 1
                    return JsonResponse(response)
                else:
                    competition = Competition.objects.find(title=title, organizer=request.user.username)
                    if competition.jury_list is not None:
                        competition.jury_list = competition.jury_list + "," + jury
                    else:
                        competition.jury_list = jury
                    competition.save()
                    JuryFile.objects.create(jury=jury, competition=title)
                response['msg'] = 'success'
                response['error_num'] = 0
            except:
                response['msg'] = 'error'
                response['error_num'] = 1
            return JsonResponse(response)
        response['msg'] = 'not POST'
        response['error_num'] = 1
        return JsonResponse(response)
    response['msg'] = 'not log in'
    response['error_num'] = 1
    return JsonResponse(response)


def my_logout(request):
    response = {}
    try:
        logout(request)
        response['msg'] = 'success'
        response['error_num'] = 0
    except:
        response['msg'] = 'logout failed'
        response['error_num'] = 1
    return JsonResponse(response)


def search_competition(request):
    response = []
    org = {}
    if request.method == "POST":
        to_search = request.POST.get("to_search")
        competition_list = Competition.objects.filter(Q(title__contains=to_search) | Q(type__contains=to_search))
        if competition_list is not None:
            for competition in competition_list:
                org['title'] = competition.title
                org['type'] = competition.type
                org['msg'] = 'success'
                org['error_num'] = 0
                response.append(org)
                return JsonResponse(response)
            org['msg'] = 'no result'
            org['error_num'] = 1
            response.append(org)
            return JsonResponse(response)
    org['msg'] = 'failed'
    org['error_num'] = 1
    response.append(org)
    return JsonResponse(response)



