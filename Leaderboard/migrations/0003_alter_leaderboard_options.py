# Generated by Django 4.1.5 on 2023-01-14 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leaderboard', '0002_alter_leaderboard_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderboard',
            options={'ordering': ['-playtime']},
        ),
    ]
