# Generated by Django 5.0.4 on 2024-05-01 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0003_alter_actor_nationality'),
        ('genres', '0002_genre_delete_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=2500)),
                ('release_date', models.DateField()),
                ('actors', models.ManyToManyField(related_name='movies', to='actors.actor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre')),
            ],
        ),
    ]