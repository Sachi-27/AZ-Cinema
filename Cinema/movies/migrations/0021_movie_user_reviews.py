# Generated by Django 4.1.3 on 2022-11-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_alter_movie_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user_reviews',
            field=models.JSONField(null=True),
        ),
    ]
