from django.contrib import admin
from brewlog.models import Recipe, BrewDay, FermentationStep, Extract, SteepingGrain, SpecialtyGrain, BaseGrain, Hop, Adjunct, OtherIngredient, Yeast

class FermentationInline(admin.TabularInline):
    model = FermentationStep
    extra = 0

class YeastInline(admin.TabularInline):
    model = Yeast
    extra = 0

class ExtractInline(admin.TabularInline):
    model = Extract
    extra = 0

class SteepingGrainInline(admin.TabularInline):
    model = SteepingGrain
    extra = 0

class SpecialtyGrainInline(admin.TabularInline):
    model = SpecialtyGrain
    extra = 0

class BaseGrainInline(admin.TabularInline):
    model = BaseGrain
    extra = 0


class HopInline(admin.TabularInline):
    model = Hop
    extra = 0

class AdjunctInline(admin.TabularInline):
    model = Adjunct
    extra = 0

class OtherIngredientInline(admin.TabularInline):
    model = OtherIngredient
    extra = 0

class BrewAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['question']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #    ]
    list_display = ('name', 'style', 'date')
    inlines = [FermentationInline,HopInline,YeastInline,ExtractInline,SteepingGrainInline,SpecialtyGrainInline,BaseGrainInline,AdjunctInline,OtherIngredientInline]
    list_filter = ['style', 'date']
    search_fields = ['name', 'notes', 'style']
    date_hierarchy = 'date'

class RecipeAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['question']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #    ]
    list_display = ('name', 'style')
    inlines = [FermentationInline,HopInline,YeastInline,ExtractInline,SteepingGrainInline,SpecialtyGrainInline,BaseGrainInline,HopInline,AdjunctInline,OtherIngredientInline]
    list_filter = ['style']
    search_fields = ['name', 'notes', 'style']

admin.site.register(BrewDay, BrewAdmin)
admin.site.register(Recipe, RecipeAdmin)

