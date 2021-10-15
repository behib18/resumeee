# Generated by Django 3.1.2 on 2021-10-15 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techskills',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]