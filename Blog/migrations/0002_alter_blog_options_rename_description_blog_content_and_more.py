# Generated by Django 4.1.5 on 2023-01-14 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['title'], 'verbose_name': 'Blogpost', 'verbose_name_plural': 'Blogposts'},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='title',
        ),
    ]