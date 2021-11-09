from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=1000)
    doc_display = models.BooleanField(default=False)
    # if run = True
    # means you can run the prject here(online)
    document = models.FileField(blank=True, upload_to='doc')

    def __str__(self):
        return self.name


class Photo(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.image.url


class Video(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    caption = models.CharField(max_length=150, blank=True)
    video = models.FileField(upload_to='video')
