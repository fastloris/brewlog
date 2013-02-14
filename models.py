from django.db import models

# Create your models here.

class Brew(models.Model):
    brewer = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    style = models.CharField(max_length=200)
    notes = models.CharField(max_length=3000)
    totalboil = models.IntegerField('Total Boil (m)')
    totalsteep = models.IntegerField('Total Steep (m)')
    notes = models.CharField(max_length=3000)
    targetog = models.DecimalField('Target OG',decimal_places=4,max_digits=6)
    targetfg = models.DecimalField('Target FG',decimal_places=4,max_digits=6)

class Recipe(Brew):
    instructions = models.CharField(max_length=3000)

class BrewDay(Brew):
    date = models.DateField()
    og = models.DecimalField('OG',decimal_places=4,max_digits=6)
    fg = models.DecimalField('FG',decimal_places=4,max_digits=6)    

# the following objects are part of a single brew

class FermentationStep(models.Model):
    def __unicode__(self):
        return self.name
    ref = models.ForeignKey(Brew)
    name = models.CharField(max_length=80)
    order = models.IntegerField()
    days = models.IntegerField()
    notes = models.CharField(max_length=3000)

# ingredients

class Ingredient(models.Model):
    def __unicode__(self):
        return self.name
    ref = models.ForeignKey(Brew)
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    
class Extract(Ingredient):
    starttime = models.IntegerField('Start Time (m)')

class SteepingGrain(Ingredient):
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Hop(Ingredient):
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Adjunct(Ingredient):
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class OtherIngredient(Ingredient):
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Yeast(Ingredient):
    fermentation_step = models.IntegerField()








