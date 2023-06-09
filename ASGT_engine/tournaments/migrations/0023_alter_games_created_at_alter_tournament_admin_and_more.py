# Generated by Django 4.1.6 on 2023-02-20 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0022_remove_tournament_player9_alter_games_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 13, 36, 27, 266856, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='admin',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 13, 36, 27, 267168, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Heure de début'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_infos',
            field=models.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 13, 36, 27, 266561, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
