# Generated by Django 4.1.3 on 2022-11-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_remove_movie_user_reviews_movie_user_reviews_imdb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='actor_image',
            field=models.CharField(max_length=500),
        ),
    ]
