from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model


class Team(Model):
    name = CharField(max_length=64)

    class Meta:
        app_label = 'tournament'


class Coach(Model):
    name = CharField(max_length=48)
    experience = IntegerField()
    team = ForeignKey(Team, on_delete=CASCADE)

    class Meta:
        app_label = 'tournament'
