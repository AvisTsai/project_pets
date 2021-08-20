# Generated by Django 3.2.5 on 2021-08-01 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0013_alter_money_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='category',
            field=models.CharField(choices=[('food', '食物'), ('toy', '玩具'), ('clothes', '衣服'), ('salon', '美容'), ('others', '其他')], default='未分類', max_length=255),
        ),
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 1, 12, 43, 58, 647569, tzinfo=utc)),
        ),
    ]
