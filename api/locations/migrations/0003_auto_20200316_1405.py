# Generated by Django 3.0.4 on 2020-03-16 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20200313_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studyarea',
            options={'ordering': ['name']},
        ),
    ]
