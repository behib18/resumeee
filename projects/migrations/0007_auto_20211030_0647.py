# Generated by Django 3.1.2 on 2021-10-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20211028_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='run',
            new_name='doc_display',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ckilck',
        ),
        migrations.AddField(
            model_name='project',
            name='document',
            field=models.FileField(blank=True, upload_to='doc'),
        ),
    ]
