# Generated by Django 2.2.7 on 2020-08-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20200803_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forreser',
            name='session_duration',
            field=models.FloatField(blank=True, help_text='ساعة', null=True, verbose_name='مدة الجلسة'),
        ),
    ]
