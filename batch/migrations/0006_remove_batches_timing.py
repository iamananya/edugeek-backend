# Generated by Django 4.0.3 on 2022-07-14 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0005_remove_courses_tumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batches',
            name='timing',
        ),
    ]
