# Generated by Django 5.0.1 on 2024-02-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_anime_list', '0002_alter_anime_episodes_alter_anime_my_episode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='is_watched',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='anime',
            name='real_rating',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='watched_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]