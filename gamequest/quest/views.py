from django.views.generic.edit import CreateView
from gamequest.quest.models import Stage, Choice, PlayerRecord
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic


class NewPlayer(CreateView):
    """Create new player & add data to session."""
    form_model      = PlayerRecord
    success_url     = reverse_lazy("stage")
    template_name   = "newplayer.html"

class DetailView(generic.DetailView):
    model = Stage
    template_name = 'quest/detail.html'