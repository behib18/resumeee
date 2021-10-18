from django.db import models


class Background(models.Model):
    description = models.TextField(max_length=200)


class Summary(models.Model):
    description = models.TextField(max_length=200)

class Education(models.Model):
    title = models.CharField(max_length=150)
    institute_name = models.CharField(max_length=150)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
