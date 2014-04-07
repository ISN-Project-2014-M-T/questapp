from django.db import models

class Stage(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    question = models.CharField(max_length=200)

class Choice(models.Model):
    stage = models.ForeignKey(Stage)
    proposition = models.CharField(max_length=200)
    redirection = models.IntegerField(default=0)

class monster(models.Model):
    stage = models.ForeignKey(Stage)
    name = models.CharField(blank=True, max_length=200)
    life = models.IntegerField(default=0)
    image = models.CharField(max_length=120)


class PlayerRecord(models.Model):
    name    = models.CharField(max_length=60)
    email   = models.EmailField(max_length=120)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.email)

    class Meta:
        ordering        = ["id"]
        unique_together = [["name", "email"]]
