"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import models
import datetime

class CreateRecipe(TestCase):
    def test_create(self):
        r = models.Recipe
        r.brewer = "Jason"
        r.name = "Test Recipe"
        r.notes = "Test Notes"
        r.style = "Test Style"
        r.targetfg = 1
        r.targetog = 2
        r.totalboil = 60
        r.totalsteep = 60
        assert(r)

class CreateBrewDay(TestCase):
    def test_create(self):
        r = models.BrewDay
        r.brewer = "Jason"
        r.name = "Test Recipe"
        r.notes = "Test Notes"
        r.style = "Test Style"
        r.targetfg = 1
        r.targetog = 2
        r.totalboil = 60
        r.totalsteep = 60
        r.date = datetime.date.today()
        r.og = 2
        r.fg = 1
        assert(r)

class createYeast(TestCase)
    def test_create(self):
        y = models.Yeast
        y.manufacturer_id = "12345"
        y.name = "Test Yeast"
        assert(y)

class createFermentationStep(TestCase)
    def test_create(self):
        fs1 = models.FermentationStep
        fs1.days = 10
        fs1.name = "Primary"
        fs1.notes = "None"
        fs1.order = 0

