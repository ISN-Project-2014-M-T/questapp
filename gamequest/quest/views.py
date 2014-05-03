from gamequest.quest.models import Stage
from django.http import Http404
from django.views import generic
from django.shortcuts import render

class DetailView(generic.DetailView):
    model = Stage
    template_name = 'quest/detail.html'

def index(request):
    return render(request, 'quest/index.html')