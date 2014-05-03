from django.db import models

class Stage(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    question = models.CharField(max_length=200)
    gain = models.IntegerField(default=0)
    perte = models.IntegerField(default=0)
    weapon = models.IntegerField(default=0)

class Choice(models.Model):
    stage = models.ForeignKey(Stage)
    proposition = models.CharField(max_length=200)
    redirection = models.IntegerField(default=0)

class monster(models.Model):
    stage = models.ForeignKey(Stage)
    name = models.CharField(blank=True, max_length=200)
    life = models.IntegerField(default=0)
    taux = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    loose = models.IntegerField(default=0)