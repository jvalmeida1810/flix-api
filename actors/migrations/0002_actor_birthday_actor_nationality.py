# Generated by Django 5.0.4 on 2024-05-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil')], max_length=100, null=True),
        ),
    ]
