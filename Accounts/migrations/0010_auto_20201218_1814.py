# Generated by Django 3.1.3 on 2020-12-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='class_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
