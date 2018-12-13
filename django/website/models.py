from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    type_choices = (
        ('Comp', 'Competitor'),
        ('Org', 'Organizer'),
        ('Rat', 'jury'),
        ('SU', 'Super User'),
    )
    user_type = models.CharField(max_length=20, choices=type_choices, default='Comp')
    salt = models.CharField(max_length=128, default=' ')


class Competitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniq_id = models.IntegerField()
    competition_list = models.TextField()

    # basic_info:
    school = models.CharField(max_length=128)


class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    competition_list = models.TextField()

    STATUS_UNCONFIRM = 0
    STATUS_CONFIRMED = 1


class Jury(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    competition_list = models.TextField()


class SuperUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Competition(models.Model):
    # basic_info:
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    description = models.TextField(default="")
    stage = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    sign_up_start = models.DateTimeField()
    sign_up_end = models.DateTimeField()
    start_time = models.TextField(default="")
    end_time = models.TextField(default="")

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
    username = models.CharField(max_length=128)
    competition = models.CharField(max_length=128)
    file_url = models.CharField(max_length=128)
    grade = models.IntegerField(default=0)
    jury_count = models.FloatField()


class JuryFile(models.Model):
    file_list = models.TextField()
    jury = models.CharField(max_length=128)
    competition = models.CharField(max_length=128)
    file_count = models.IntegerField()
    finished_count = models.IntegerField()


'''class OrgCompetition(models.Model):
    title = models.CharField(max_length=128)
    organizer = models.ForeignKey(Organizer)
    stage = models.IntegerField()
    description = models.TextField()

    STATUS_PREPARE = 0
    STATUS_PRELIMINARY = 1
    STATUS_SEMIFINALS = 2
    STATUS_FINAL = 3
    STATUS_SUSPEND = 4
    STATUS_END = 5


class UserCompetition(models.Model):
    title = models.CharField(max_length=128)
    file_url = models.URLField()
    grade = models.IntegerField()
    competiton = models.ForeignKey(OrgCompetition)
    competitor = models.OneToOneField(User)
    jury = models.ManyToManyField(jury)'''


