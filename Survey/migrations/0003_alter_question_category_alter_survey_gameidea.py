# Generated by Django 4.1.5 on 2023-01-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0002_alter_survey_gameidea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], max_length=2),
        ),
        migrations.AlterField(
            model_name='survey',
            name='gameidea',
            field=models.CharField(choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], default=3, max_length=1),
        ),
    ]
