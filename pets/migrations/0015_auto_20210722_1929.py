# Generated by Django 3.2.4 on 2021-07-22 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0014_auto_20210722_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 11, 29, 31, 319041, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='register',
            name='check_password',
            field=models.CharField(max_length=15, verbose_name='請再輸入一次密碼'),
        ),
        migrations.AlterField(
            model_name='register',
            name='user_email',
            field=models.CharField(max_length=20, verbose_name='請輸入你的電子郵件'),
        ),
        migrations.AlterField(
            model_name='register',
            name='user_pwd',
            field=models.CharField(max_length=15, verbose_name='請輸入你的密碼'),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=15, verbose_name='請輸入你的帳號'),
        ),
    ]
