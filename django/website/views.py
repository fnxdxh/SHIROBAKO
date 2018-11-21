from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from datetime import datetime
from django.utils import timezone
from django.contrib import auth
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User, Competitor, Organizer, Rator, Competition, UserFile, SuperUser, RatorFile
# Create your views here.


def may_use(request):
    now_time = str(datetime.now())
    return render(request, 'hello_world.html', {'current_time': now_time})


def index(request):
    return render(request, '首页.html')


def competitor_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = User.objects.create_user(username=username, password=password)
                competitor = Competitor.objects.create(user=user)
                return HttpResponse("register success")
            except:
                return HttpResponse("register failed")
        return HttpResponse("register failed")
    return HttpResponse("register failed")


def rator_register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            try:
                user = User.objects.create_user(username=username, password=password)
                competitor = Rator.objects.create(user=user)
                return HttpResponse("register success")
            except:
                return HttpResponse("register failed")
        return HttpResponse("register failed")
    return HttpResponse("register failed")


def organizer_register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            try:
                user = User.objects.create_user(username=username, password=password)
                organizer = Organizer.objects.create(user=user, status=Organizer.STATUS_UNCONFIRM)
                return HttpResponse("register success")
            except:
                return HttpResponse("register failed")
        return HttpResponse("register failed")
    return HttpResponse("register failed")


def competitor_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    competitor = Competitor.objects.find(user=user)
                    login(request, user)
                    return HttpResponse("competitor login success")
                except:
                    return HttpResponse("competitor login failed")
            return HttpResponse("user not exist")
        return HttpResponse("username or password is none")
    return HttpResponse("false method")


def organizer_login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    organizer = Organizer.objects.find(user=user)
                    if organizer.status == Organizer.STATUS_CONFIRMED:
                        login(request, user)
                        return HttpResponse("organizer login success")
                    elif organizer.status == Organizer.STATUS_UNCONFIRM:
                        return HttpResponse("organizer didn't confirm")
                except:
                    return HttpResponse("orgnizer login failed")
            return HttpResponse("user not exist")
        return HttpResponse("username or password is none")
    return HttpResponse("false method")


def rator_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    rator = Rator.objects.find(user=user)
                    login(request, user)
                    return HttpResponse("rator login success")
                except:
                    return HttpResponse("rator login failed")
            return HttpResponse("user not exist")
        return HttpResponse("username or password is none")
    return HttpResponse("false method")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return HttpResponse("rator login success")
                return HttpResponse("not superuser")
            return HttpResponse("user not exist")
        return HttpResponse("username or password is none")
    return HttpResponse("false method")


def index_competition_list(request):
    now_time = timezone.now()
    competition_list = Competition.objects.filter(Q(sign_up_start__gte=now_time + datetime.timedelta(days=7)) &
                                                  Q(sign_up_end__lt=now_time))
    if competition_list is not None:
        response = []
        for competition in competition_list:
            cmp = {}
            cmp['title'] = competition.title
            cmp['organizer'] = competition.organizer
            cmp['type'] = competition.type
            start_time_list = competition.start_time.split(',')
            cmp['start_time'] = start_time_list[0]
            end_time_list = competition.end_time.split(',')
            cmp['end_time'] = end_time_list[-1]
            response.append(cmp)
        return JsonResponse(response)
    return HttpResponse("recent no competition")


def competitor_competition_list(request):
    if request.user.is_authenticated():
        try:
            competitor = Competitor.objects.find(user=request.user)
            competition_list = competitor.activity_list.split(',')
            response = []
            if competition_list is not None:
                for title in competition_list:
                    org = {}
                    org['title'] = title
                    response.append(org)
                return JsonResponse(response)
            return HttpResponse("not sign up any Competition")
        except:
            return HttpResponse("No User")
    return HttpResponse("not log in")


def rator_competition_list(request):
    if request.user.is_authenticated():
        try:
            #rator = Rator.objects.find(user=request.user)
            rator = request.user.rator
            competition_list = rator.activity_list.split(',')
            response = []
            if competition_list is not None:
                for title in competition_list:
                    org = {}
                    org['title'] = title
                    response.append(org)
                return JsonResponse(response)
            return HttpResponse("not sign up any Competition")
        except:
            return HttpResponse("No User")
    return HttpResponse("not log in")


def organizer_competition_list(request):
    if request.user.is_authenticated():
        try:
            #organizer = Competitor.objects.find(user=request.user)
            organizer = request.user.organizer
            competition_list = organizer.activity_list.split(',')
            response = []
            if competition_list is not None:
                for title in competition_list:
                    org = {}
                    org['title'] = title
                    response.append(org)
                return JsonResponse(response)
            return HttpResponse("not sign up any Competition")
        except:
            return HttpResponse("No User")
    return HttpResponse("not log in")


def competitor_sign_up(request):
    if request.user.is_authenticated():
        competitor = request.user.competitor
        if request.method == "POST":
            name = request.POST.get("competition_name")
            try:
                competition = Competition.objects.find(title=name)
                if competition.competitor_list is not None:
                    competition.competitor_list = competition.competitor_list + "," + str(competitor.uniq_id)
                else:
                    competition.competitor_list = str(competitor.uniq_id)
                competition.save()
                if competitor.competition_list is not None:
                    competitor.competition_list = competitor.competition_list + "," + name
                else:
                    competitor.competition_list = name
                competitor.save()
                return HttpResponse("Sign up success")
            except:
                return HttpResponse('Sign up failed')
        return HttpResponse("method failed")
    return HttpResponse("not log in")


# 参考：https://www.jianshu.com/p/1a5546ce0c92
def file_upload(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            file = request.FILES.get("file")
            competition = request.POST.get("competition_name")
            with open(file.name, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            competitor = request.user.competitor
            try:
                file = UserFile.objects.find(username=request.user.username, competition=competition)
                file.file_url = file.name
                file.save()
                return HttpResponse("Upload Success 2")
            except:
                UserFile.objects.create(username=request.user.username, competition=competition, file_url=file.name)
                return HttpResponse("Upload success 1")
        return HttpResponse("method wrong")
    return HttpResponse("not log in")


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
    if request.user.is_authenticated():
        if request.method == "POST":
            grade = request.POST.get("grade")
            file_url = request.POST.get("filepath")
            try:
                file = UserFile.objects.find(file_url=file_url)
                file.grade = file.grade + grade / file.rator_count
                file.save()
                return HttpResponse("upload success")
            except:
                return HttpResponse("upload fail")
        return HttpResponse("method wrong")
    return HttpResponse("not log in")


def file_list(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            competition = request.POST.get("competition_name")
            try:
                rator_file = RatorFile.objects.find(competition=competition, rator=request.user.username)
                file_list = rator_file.file_list.split(",")
                response = []
                for file in file_list:
                    response.append(file)
                return JsonResponse(response)
            except:
                return HttpResponse("no file to grade")
        return HttpResponse("method wrong")
    return HttpResponse("not log in")


def competition_detail(request):
    if request.method == "POST":
        activity_name = request.POST.get("competition_title")
        try:
            activity = Competition.objects.find(title=activity_name)
            response = []
            detail = {}
            detail['title'] = activity.title
            detail['stage'] = activity.stage
            detail['organizor'] = activity.organizor.name
            detail['description'] = activity.description
            response.append(detail)
            return JsonResponse(response)
        except:
            return HttpResponse("load error")


def admin_to_confirm_list(request):
    organizers = Organizer.objects.filter(status=Organizer.STATUS_UNCONFIRM)
    organizer_list = []
    for organizer in organizers:
        org = {}
        org['username'] = organizer.username
        organizer_list.append(org)
    return JsonResponse(organizer_list)


def admin_to_confirm(request):
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            organizer = Organizer.objects.find(username=username, status=Organizer.STATUS_UNCONFIRM)
            organizer.status = Organizer.STATUS_CONFIRMED
            organizer.save()
        except:
            return HttpResponse("no user")
    return HttpResponse("method wrong")


def divide_test_paper(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            title = request.POST.get("competition_name")
            try:
                competition = Competition.objects.find(title=title, organizer=request.user.username)
                user_list = competition.competitor_list.split(",")
                rator_list = competition.rator_list.split(",")
            except:
                return HttpResponse("divide fail")
        return HttpResponse("method wrong")
    return HttpResponse("not log in")



def create_competition(request):
    response = {}
    if request.user.is_authenticated():
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            stage = request.POST.get("stage")
            # there are some information of the competition
            organizer = request.user.username
            try:
                competiton = Competition.objects.create(title=title, description=description, stage=stage,
                                                        organizer=organizer)
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


def invite_rator(request):
    response = {}
    if request.user.is_authenticated():
        if request.method == "POST":
            rator = request.POST.get("rator")
            title = request.POST.get("competition_name")
            try:
                competition = Competition.objects.find(title=title, organizer=request.user.username)
                if competition.rator_list is not None:
                    competition.rator_list = competition.rator_list + "," + rator
                else:
                    competition.rator_list = rator
                competition.save()
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


