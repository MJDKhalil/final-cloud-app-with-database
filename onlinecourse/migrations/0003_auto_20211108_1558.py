# Generated by Django 3.2.9 on 2021-11-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20211108_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AddField(
            model_name='submission',
            name='choices',
            field=models.ManyToManyField(to='onlinecourse.Choice'),
        ),
    ]
