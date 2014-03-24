from django.db import models

class Stage(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    question = models.CharField(max_length=200)

class Choice(models.Model):
    stage = models.ForeignKey(Stage)
    proposition = models.CharField(max_length=200)
    redirection = models.IntegerField(default=0)