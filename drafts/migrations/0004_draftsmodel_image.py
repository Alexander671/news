# Generated by Django 3.2 on 2021-12-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0003_auto_20211224_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftsmodel',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
