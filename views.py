# Create your views here.

from brewlog.models import BrewDay
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def index(request):
    latest_brewday_list = BrewDay.objects.order_by('-date')[:5]
    context = {'latest_brewday_list': latest_brewday_list}
    return render(request, 'brewlog/index.html', context)

def detail(request, brewday_id):
    brewday = get_object_or_404(BrewDay, pk=brewday_id)
    return render(request, 'brewlog/detail.html', {'brewday': brewday})