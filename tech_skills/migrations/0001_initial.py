# Generated by Django 3.2.9 on 2021-11-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherTechSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TechSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('quality', models.CharField(choices=[('basic', 'basic'), ('lower intermediate', 'lower intermediate'), ('intermediate', 'intermediate'), ('upper intermediate', 'upper intermediate'), ('advance', 'advance'), ('expert', 'expert')], default='basic', max_length=20)),
            ],
        ),
    ]
