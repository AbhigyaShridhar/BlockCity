# Generated by Django 3.2.3 on 2021-08-21 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210821_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.city')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='country_code',
            field=models.IntegerField(default=91),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('matches', models.IntegerField(default=0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.city')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('matches', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('xp', models.IntegerField(default=0)),
                ('captain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.school')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='match_date')),
                ('upcoming', models.BooleanField(default=True)),
                ('past', models.BooleanField(default=False)),
                ('refree', models.CharField(blank=True, max_length=100, null=True)),
                ('tie', models.BooleanField(default=False)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='backend.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='backend.team')),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.venue')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.team')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.school'),
        ),
    ]