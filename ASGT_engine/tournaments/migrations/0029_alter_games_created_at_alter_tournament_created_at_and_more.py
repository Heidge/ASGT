# Generated by Django 4.1.6 on 2023-02-23 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0028_alter_games_created_at_alter_tournament_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 9, 47, 16, 630867, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 9, 47, 16, 631131, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 9, 47, 16, 630519, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
