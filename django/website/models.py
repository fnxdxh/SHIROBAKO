from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    type_choices = (
        ('Comp', 'Competitor'),
        ('Org', 'Organizer'),
        ('Rat', 'Jury'),
        ('SU', 'SuperUser'),
    )
    user_type = models.CharField(max_length=20, choices=type_choices, default='Comp')
    unique_id = models.CharField(max_length=128, default='')


class Competitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    competition_list = models.TextField(default='')

    # basic_info:
    school = models.CharField(max_length=128,default="")
    age = models.CharField(max_length=20,default="")
    tel = models.CharField(max_length=20,default="")
    email = models.CharField(max_length=128, default='')

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    competition_list = models.TextField(default='')

# basic
    tel = models.CharField(max_length=20,default="")
    email = models.CharField(max_length=128, default='')

    STATUS_UNCONFIRM = 0
    STATUS_CONFIRMED = 1


class Jury(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    competition_list = models.TextField(default='')

    school = models.CharField(max_length=128,default="")
    tel = models.CharField(max_length=20,default="")
    email = models.CharField(max_length=128, default='')

class SuperUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Competition(models.Model):
    # basic_info:
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128,default="")
    description = models.TextField(default="")
    stage = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    sign_up_start = models.DateTimeField()
    sign_up_end = models.DateTimeField()
    #start_time = models.TextField(default='')
    #end_time = models.TextField(default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    sponsor = models.CharField(max_length=128, default="")

    organizer = models.CharField(max_length=128)
    competitor_list = models.TextField(default="")
    jury_list = models.TextField(default="")

    STATUS_PREPARE = 0
    STATUS_PRELIMINARY = 1
    STATUS_SEMIFINALS = 2
    STATUS_FINAL = 3
    STATUS_SUSPEND = 4
    STATUS_END = 5


class UserFile(models.Model):
    username = models.CharField(max_length=128,default='')
    competition = models.CharField(max_length=128,default='')
    file_url = models.CharField(max_length=128,default='')
    grade_list = models.CharField(max_length=128,default="")
    jury_list = models.CharField(max_length=128,default="")
    grade = models.FloatField(default=0.0)
    jury_count = models.IntegerField(default=0)


class JuryFile(models.Model):
    file_list = models.TextField(default='')
    jury = models.CharField(max_length=128,default='')
    competition = models.CharField(max_length=128,default='')
    file_count = models.IntegerField(default=0)
    finished_count = models.IntegerField(default=0)



