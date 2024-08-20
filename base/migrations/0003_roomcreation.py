# Generated by Django 5.1 on 2024-08-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
