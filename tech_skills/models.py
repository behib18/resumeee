from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class TechSkills(models.Model):
    skill = models.CharField(max_length=50)
    quantity = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)])


class OtherTechSkills(models.Model):
    skill = models.CharField(max_length=70)
