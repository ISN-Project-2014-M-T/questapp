from gamequest.quest.models import Stage
from django.http import Http404
from django.views import generic


class DetailView(generic.DetailView):
    model = Stage
    template_name = 'quest/detail.html'