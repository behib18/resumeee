from django.db import models

class Summary(models.Model):
    description = models.TextField(max_length=200)
