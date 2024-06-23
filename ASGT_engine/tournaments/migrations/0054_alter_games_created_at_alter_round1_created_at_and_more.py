# Generated by Django 5.0.6 on 2024-06-23 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0053_alter_games_created_at_alter_round1_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 15, 15, 42, 435202, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 15, 15, 42, 436201, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='round2',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 15, 15, 42, 436708, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='round2',
            name='player1',
            field=models.CharField(default='Vainqueur match 1', max_length=20, null=True, verbose_name='Joueur 1'),
        ),
        migrations.AlterField(
            model_name='round3',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 15, 15, 42, 436708, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 15, 15, 42, 435702, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 15, 15, 42, 435202, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
