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


class Experience(models.Model):
    title = models.CharField(max_length=150)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    description = models.TextField(max_length=500)

class Licence(models.Model):
    title = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)

class Language(models.Model):
    title = models.CharField(max_length=150)
    level = models.CharField(max_length=80)
    description = models.TextField(max_length=500, blank=True)