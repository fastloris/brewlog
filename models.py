from django.db import models
import datetime

# Create your models here.

class Brew(models.Model):
    def __unicode__(self):
        return self.name
    brewer = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    style = models.CharField(max_length=200)
    notes = models.TextField()
    totalboil = models.IntegerField('Total Boil (m)')
    totalsteep = models.IntegerField('Total Steep (m)')
    totalmash = models.IntegerField('Total Mash (m)')
    targetog = models.DecimalField('Target OG',decimal_places=4,max_digits=6)
    targetfg = models.DecimalField('Target FG',decimal_places=4,max_digits=6)
    targetabv = models.DecimalField('Target ABV',decimal_places=2,max_digits=5)

class Recipe(Brew):
    instructions = models.TextField()

class BrewDay(Brew):
    date = models.DateField()
    og = models.DecimalField('OG',decimal_places=4,max_digits=6)
    fg = models.DecimalField('FG',decimal_places=4,max_digits=6)
    abv = models.DecimalField('ABV',decimal_places=2,max_digits=6)
    recipe_used = models.ForeignKey(Recipe,blank=True,null=True)
    def remaining_days(self):
        now = datetime.date.today()
        due = self.due_date()
        difference = due - now
        if (difference.days <= 0):
            return 0
        else:
            return difference.days
    def total_days(self):
        totaldays = 0
        for fermentationstep in self.fermentationstep_set.all():
            totaldays = totaldays + fermentationstep.days
        return (totaldays)
    def due_date(self):
        return (self.date + datetime.timedelta(days=self.total_days()))

# the following objects are part of a single brew

class FermentationStep(models.Model):
    def __unicode__(self):
        return self.name
    ref = models.ForeignKey(Brew)
    name = models.CharField(max_length=80)
    order = models.IntegerField()
    days = models.IntegerField()
    notes = models.TextField()

# ingredients

class Extract(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')

class SteepingGrain(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class SpecialtyGrain(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    mash_temp = models.IntegerField()
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class BaseGrain(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    mash_temp = models.IntegerField()
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Hop(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Adjunct(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class OtherIngredient(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    ref = models.ForeignKey(Brew)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Yeast(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    fermentation_step = models.IntegerField()
    ref = models.ForeignKey(Brew)


