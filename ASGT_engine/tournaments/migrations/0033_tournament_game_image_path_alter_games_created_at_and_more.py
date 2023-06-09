# Generated by Django 4.1.7 on 2023-02-24 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0032_alter_games_created_at_alter_tournament_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='game_image_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 9, 56, 21, 232026, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 9, 56, 21, 232189, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 9, 56, 21, 231803, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
