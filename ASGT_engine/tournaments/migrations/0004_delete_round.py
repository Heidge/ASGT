# Generated by Django 4.1.6 on 2023-02-09 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_round_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Round',
        ),
    ]
