# Generated by Django 4.0.5 on 2022-09-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp22', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]