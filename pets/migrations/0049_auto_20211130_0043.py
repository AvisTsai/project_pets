# Generated by Django 3.2.9 on 2021-11-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0048_shop_shop_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_price',
            field=models.CharField(max_length=20, verbose_name='價格'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_title',
            field=models.CharField(max_length=50, verbose_name='標題'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_url',
            field=models.CharField(default='', max_length=255, verbose_name='圖片網址'),
        ),
    ]
