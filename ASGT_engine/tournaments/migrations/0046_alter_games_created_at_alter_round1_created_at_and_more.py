# Generated by Django 4.1.6 on 2024-01-11 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0045_remove_tournament_tournament_infos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 15, 33, 19, 557619, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 15, 33, 19, 558618, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player1_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 1'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player2_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 2'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player3_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 3'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player4_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 4'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player5_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 5'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player6_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 6'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player7_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 7'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='player8_score',
            field=models.IntegerField(null=True, verbose_name='Score joueur 8'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 15, 33, 19, 557619, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 15, 33, 19, 556653, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
