# Generated by Django 3.1.2 on 2021-10-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_skills', '0003_remove_techskills_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherTechSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=70)),
            ],
        ),
    ]