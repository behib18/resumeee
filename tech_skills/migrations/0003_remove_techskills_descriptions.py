# Generated by Django 3.1.2 on 2021-10-15 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech_skills', '0002_auto_20211015_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techskills',
            name='descriptions',
        ),
    ]