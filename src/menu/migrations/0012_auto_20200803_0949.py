# Generated by Django 2.2.7 on 2020-08-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_numberofseats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofseats',
            name='number_of_seats1',
            field=models.CharField(blank=True, max_length=10, verbose_name='عدد المقاعد'),
        ),
        migrations.AlterField(
            model_name='sessiontype',
            name='session_type1',
            field=models.CharField(blank=True, max_length=30, verbose_name='نوع الجلسة'),
        ),
    ]
