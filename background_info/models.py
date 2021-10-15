from django.db import models

class Background(models.Model):
    description = models.TextField(max_length=200)
