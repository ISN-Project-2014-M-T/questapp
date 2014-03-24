from django.conf.urls import patterns, url

from gamequest.quest import views

urlpatterns = patterns('',
    url(r"^$", views.NewPlayer.as_view(), name='newplayer'),
)