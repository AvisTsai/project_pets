# Generated by Django 3.2.2 on 2021-05-07 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OriginPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名稱')),
            ],
            options={
                'verbose_name': '產地',
                'verbose_name_plural': '產地',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='名稱')),
            ],
            options={
                'verbose_name': '標籤',
                'verbose_name_plural': '標籤',
            },
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名稱')),
                ('description', models.TextField(verbose_name='描述')),
                ('roast', models.CharField(choices=[('Light', '極淺度烘焙'), ('Cinnamon', '淺度烘焙'), ('Medium', '中度烘焙'), ('High', '中度微深烘焙'), ('City', '中深度烘焙'), ('Full-City', '微深度烘焙'), ('French', '極深烘焙'), ('Italian', '極深度烘焙')], max_length=10, verbose_name='尺寸')),
                ('price', models.PositiveIntegerField(verbose_name='價格')),
                ('origin_place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets.originplace', verbose_name='種類')),
                ('tags', models.ManyToManyField(to='pets.Tag', verbose_name='標籤')),
            ],
            options={
                'verbose_name': '咖啡豆',
                'verbose_name_plural': '咖啡豆',
            },
        ),
    ]
