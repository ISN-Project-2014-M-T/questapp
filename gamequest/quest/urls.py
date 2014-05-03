from django.conf.urls import patterns, url

from gamequest.quest import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.index, name='index'),
)