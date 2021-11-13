from django.db import models

class Contact(models.Model):
    description = models.TextField(max_length=700)