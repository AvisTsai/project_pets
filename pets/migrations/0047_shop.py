# Generated by Django 3.2.9 on 2021-11-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0046_auto_20211128_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_title', models.CharField(max_length=50, unique=True, verbose_name='標題')),
                ('shop_price', models.CharField(max_length=20, unique=True, verbose_name='價格')),
            ],
            options={
                'verbose_name': '商店',
                'verbose_name_plural': '商店',
            },
        ),
    ]
