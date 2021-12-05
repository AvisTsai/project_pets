# Generated by Django 3.2.9 on 2021-12-05 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0061_shop_produce_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='storage_token',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.register'),
        ),
    ]
