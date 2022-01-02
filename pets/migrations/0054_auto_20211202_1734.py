# Generated by Django 3.2.9 on 2021-12-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0053_merge_0031_alter_money_time_0052_merge_20211130_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='category',
            field=models.CharField(choices=[('食物', '食物'), ('玩具', '玩具'), ('衣服', '衣服'), ('美容', '美容'), ('其他', '其他')], max_length=255, verbose_name='類別'),
        ),
        migrations.AlterField(
            model_name='money',
            name='item',
            field=models.CharField(choices=[('肉乾', '肉乾'), ('鮮食', '鮮食'), ('飼料', '飼料'), ('餅乾', '餅乾'), ('潔牙骨', '潔牙骨'), ('飛盤', '飛盤'), ('球', '球'), ('繩索', '繩索'), ('玩偶', '玩偶'), ('塑膠玩具', '塑膠玩具'), ('領巾', '領巾'), ('褲裝', '褲裝'), ('裙裝', '裙裝'), ('洗澡', '洗澡'), ('剪毛', '剪毛'), ('預防針', '預防針'), ('保養品', '保養品'), ('看醫生', '看醫生'), ('項圈', '項圈')], max_length=255, verbose_name='項目'),
        ),
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]