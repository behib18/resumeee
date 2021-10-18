from django.db import models

class ContactForm(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=700)

class Contact(models.Model):
    description = models.TextField(max_length=700)