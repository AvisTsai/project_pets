# Generated by Django 3.2.4 on 2021-10-15 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0021_merge_0014_auto_20210801_2043_0020_alter_money_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
