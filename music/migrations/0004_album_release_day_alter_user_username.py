# Generated by Django 4.2 on 2023-04-17 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_rename_artist_id_album_artist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_day',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]