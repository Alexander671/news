# Generated by Django 3.2 on 2021-12-23 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autors',
            old_name='author',
            new_name='autor',
        ),
    ]