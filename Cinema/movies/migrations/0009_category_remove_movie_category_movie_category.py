# Generated by Django 4.1.3 on 2022-11-22 08:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_movie_producers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(to='movies.category'),
        ),
    ]
