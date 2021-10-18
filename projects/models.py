from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=1000)
    run = models.BooleanField(default=False)
    # if run = True
    # means you can run the prject here(online)
    ckilck = models.URLField(blank=True)


class Photo(models.Model):
    image = models.ForeignKey(
        Project, on_delete=models.CASCADE)