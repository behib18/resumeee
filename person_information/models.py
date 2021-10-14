from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r"^(\\+98)?9\\d{9}$",
    message="Phone number must be entered in the following format: '09123456789'.",
)


class PersonInfo(models.Model):
    # including first_name, last_name, username, pass, email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField()
    phone = models.CharField(
        validators=[phone_regex], max_length=11, null=True, blank=True
    )
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    home_title = models.CharField(max_length=200)
    about_title = models.CharField(max_length=200)
    bio = models.TextField(max_length=700, blank=True)
    main_description = models.TextField(max_length=900, blank=True)
    background_image = models.ImageField(upload_to='photos')
    show_image = models.ImageField(upload_to='photos')
