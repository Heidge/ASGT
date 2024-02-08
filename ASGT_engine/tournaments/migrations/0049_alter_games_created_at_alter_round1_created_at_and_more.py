# Generated by Django 4.1.6 on 2024-02-08 10:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0048_alter_games_created_at_alter_round1_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 10, 20, 19, 226379, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='round1',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 10, 20, 19, 227380, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 10, 20, 19, 227380, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 10, 20, 19, 226379, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.CreateModel(
            name='Round2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 2, 8, 10, 20, 19, 228379, tzinfo=datetime.timezone.utc), verbose_name='Créé le')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player1', models.CharField(max_length=20, null=True, verbose_name='Joueur 1')),
                ('player1_score', models.IntegerField(null=True, verbose_name='Score joueur 1')),
                ('player2', models.CharField(max_length=20, null=True, verbose_name='Joueur 2')),
                ('player2_score', models.IntegerField(null=True, verbose_name='Score joueur 2')),
                ('player3', models.CharField(max_length=20, null=True, verbose_name='Joueur 3')),
                ('player3_score', models.IntegerField(null=True, verbose_name='Score joueur 3')),
                ('player4', models.CharField(max_length=20, null=True, verbose_name='Joueur 4')),
                ('player4_score', models.IntegerField(null=True, verbose_name='Score joueur 4')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournaments.tournament', verbose_name='Tournoi')),
            ],
        ),
    ]