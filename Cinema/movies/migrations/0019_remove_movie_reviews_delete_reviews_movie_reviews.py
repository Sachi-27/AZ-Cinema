# Generated by Django 4.1.3 on 2022-11-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_reviews_movie_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviews',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.JSONField(null=True),
        ),
    ]
