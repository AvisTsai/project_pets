# Generated by Django 3.2.9 on 2021-11-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0032_auto_20211123_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('user_pwd', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': '登入',
                'verbose_name_plural': '登入',
            },
        ),
    ]
