# Generated by Django 3.2.9 on 2021-12-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0059_rename_data_time_money_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.CharField(default='請選擇時間', max_length=255),
        ),
    ]