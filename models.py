from django.db import models

# Create your models here.

# an object representing a single brew day

class BrewDay(Recipe, models.Model):
    date = models.DateField()
    brewer = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    style = models.CharField(max_length=200)
    notes = models.CharField(max_length=3000)
    totalboil = models.IntegerField('Total Boil (m)')
    totalsteep = models.IntegerField('Total Steep (m)')
    notes = models.CharField(max_length=3000)
    targetog = models.DecimalField('Target OG',decimal_places=4,max_digits=6)
    og = models.DecimalField('OG',decimal_places=4,max_digits=6)
    recipe = models.ForeignKey(Recipe,blank=True,null=True)

# the following objects are part of a single brew

class FermentationStep(models.Model):
    def __unicode__(self):
        return self.name
    brew = models.ForeignKey(BrewDay)
    name = models.CharField(max_length=80)
    order = models.IntegerField()
    days = models.IntegerField()
    notes = models.CharField(max_length=3000)
    targetfg = models.DecimalField('Target FG',decimal_places=4,max_digits=6)
    fg = models.DecimalField('FG',decimal_places=4,max_digits=6)

# parts of worts

class Extract(models.Model):
    def __unicode__(self):
        return self.name
    brew = models.ForeignKey(BrewDay)
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    addtime = models.IntegerField('Add Time (m)')

class SteepingGrain(models.Model):
    def __unicode__(self):
        return self.name
    brew = models.ForeignKey(BrewDay)
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('Start Time (m)')

class Hop(models.Model):
    def __unicode__(self):
        return self.name
    brew = models.ForeignKey(BrewDay)
    name = models.CharField(max_length=80)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')

class Adjunct(models.Model):
    def __unicode__(self):
        return self.name
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    brew = models.ForeignKey(BrewDay)
    name = models.CharField(max_length=80)
    addtime = models.IntegerField('Add Time (m)')

class OtherIngredient(models.Model):
    def __unicode__(self):
        return self.name
    brew = models.ForeignKey(BrewDay)
    weight = models.DecimalField(decimal_places=2,max_digits=6)
    weight_unit = models.CharField(max_length=8)
    name = models.CharField(max_length=80)
    starttime = models.IntegerField('Start Time (m)')
    endtime = models.IntegerField('End Time (m)')
    addtime = models.IntegerField('Add Time (m)')


# parts of fermentation

class Yeast(models.Model):
    def __unicode__(self):
        return self.name
    brew = models.ForeignKey(BrewDay)
    name = models.CharField(max_length=80)
    manufacturer_id = models.CharField(max_length=20)

class Comment(models.Model):
    def __unicode__(self):
        return self.comment
    comment = models.CharField(max_length=3000)
    email = models.CharField(max_length=30)







