# Generated by Django 4.0.5 on 2022-09-17 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp22', '0002_blogpage_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='author',
        ),
    ]
