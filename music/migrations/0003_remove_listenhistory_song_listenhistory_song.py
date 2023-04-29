# Generated by Django 4.2 on 2023-04-28 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_listenhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listenhistory',
            name='song',
        ),
        migrations.AddField(
            model_name='listenhistory',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.song'),
        ),
    ]
