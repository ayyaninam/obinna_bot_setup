# Generated by Django 5.1 on 2024-08-13 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_channel_artist_id_channel_influencer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='channel_id',
            new_name='channel',
        ),
    ]
