# Generated by Django 5.0.3 on 2024-03-17 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_repost_created_time_repost_modified_time_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='repost',
            table='repost',
        ),
        migrations.AlterModelTable(
            name='topic',
            table='topic',
        ),
    ]
