# Generated by Django 3.2.9 on 2021-11-30 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0050_alter_shop_shop_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='verify', serialize=False, to='pets.register'),
        ),
    ]