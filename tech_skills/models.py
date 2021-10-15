from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class TechSkills(models.Model):
    descriptions = models.TextField(max_length=200, blank=True)
    skill = models.CharField(max_length=50)
    quantity = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)])
