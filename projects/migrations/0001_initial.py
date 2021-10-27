# Generated by Django 3.1.2 on 2021-10-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=100)),
                ('client', models.CharField(blank=True, max_length=100)),
                ('date', models.CharField(blank=True, max_length=50)),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField(max_length=1000)),
                ('run', models.BooleanField(default=False)),
                ('ckilck', models.URLField(blank=True)),
            ],
        ),
    ]
