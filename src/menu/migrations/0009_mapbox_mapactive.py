# Generated by Django 2.2.7 on 2020-06-16 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_mapbox_mapimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapbox',
            name='mapActive',
            field=models.BooleanField(default=False),
        ),
    ]
