# Generated by Django 3.2.9 on 2021-11-28 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0043_auto_20211128_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verify', to='pets.register'),
        ),
    ]
