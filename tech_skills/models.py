from django.db import models


class TechSkills(models.Model):
    skill = models.CharField(max_length=50)
    quality_choices = (
        ('basic', 'basic'),
        ('lower intermediate', 'lower intermediate'),
        ('intermediate', 'intermediate'),
        ('upper intermediate', 'upper intermediate'),
        ('advance', 'advance'),
        ('expert', 'expert'),
    )
    quality = models.CharField(
        max_length=20, choices=quality_choices, default='basic')


class OtherTechSkills(models.Model):
    skill = models.CharField(max_length=70)
