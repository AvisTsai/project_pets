# Generated by Django 3.2.9 on 2021-11-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0047_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_url',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='圖片網址'),
        ),
    ]
