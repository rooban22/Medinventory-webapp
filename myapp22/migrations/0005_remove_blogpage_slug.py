# Generated by Django 4.0.5 on 2022-09-17 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp22', '0004_blogpage_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='slug',
        ),
    ]
