# Generated by Django 3.2.6 on 2021-08-05 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0018_alter_money_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 15, 9, 37, 741925, tzinfo=utc)),
        ),
    ]
