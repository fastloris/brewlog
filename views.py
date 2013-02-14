# Create your views here.

from brewlog.models import BrewDay, Recipe
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def brewdayindex(request):
    latest_brewday_list = BrewDay.objects.order_by('-date')[:5]
    context = {'latest_brewday_list': latest_brewday_list}
    return render(request, 'brewlog/brewindex.html', context)

def brewdaydetail(request, brewday_id):
    brewday = get_object_or_404(BrewDay, pk=brewday_id)
    return render(request, 'brewlog/brewdetail.html', {'brewday': brewday})


def recipeindex(request):
    latest_recipe_list = Recipe.objects.order_by('style')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'brewlog/recipeindex.html', context)

def recipedetail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'brewlog/recipedetail.html', {'recipe': recipe})