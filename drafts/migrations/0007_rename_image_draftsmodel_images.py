# Generated by Django 3.2 on 2021-12-26 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0006_rename_user_draft_draftsmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='draftsmodel',
            old_name='image',
            new_name='images',
        ),
    ]