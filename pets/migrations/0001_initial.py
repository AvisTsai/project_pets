# Generated by Django 3.2.4 on 2021-12-02 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='標題')),
                ('description', models.TextField()),
                ('start_time', models.DateField(default='請選擇時間')),
                ('end_time', models.DateField(default='請選擇時間')),
            ],
        ),
        migrations.CreateModel(
            name='MemberManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=20, unique=True, verbose_name='使用者ID')),
                ('UserName', models.CharField(max_length=20, unique=True, verbose_name='使用者名稱')),
                ('UserAccount', models.CharField(max_length=20, unique=True, verbose_name='使用者帳號')),
                ('UserPassword', models.CharField(max_length=20, unique=True, verbose_name='使用者密碼')),
                ('Email', models.CharField(max_length=20, unique=True, verbose_name='使用者電子郵件')),
            ],
            options={
                'verbose_name': '會員管理',
                'verbose_name_plural': '會員管理',
            },
        ),
        migrations.CreateModel(
            name='Mobject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('food', '食物'), ('toy', '玩具'), ('clothes', '衣服'), ('salon', '美容'), ('others', '其他')], max_length=255, verbose_name='類別')),
                ('item', models.CharField(choices=[('肉乾', '肉乾'), ('鮮食', '鮮食'), ('飛盤', '飛盤'), ('clothes', '領巾'), ('salon', '剪毛'), ('others', '項圈')], max_length=255, verbose_name='項目')),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default='請選擇時間')),
                ('category', models.CharField(choices=[('food', '食物'), ('toy', '玩具'), ('clothes', '衣服'), ('salon', '美容'), ('others', '其他')], max_length=255, verbose_name='類別')),
                ('item', models.CharField(choices=[('肉乾', '肉乾'), ('鮮食', '鮮食'), ('飛盤', '飛盤'), ('clothes', '領巾'), ('salon', '剪毛'), ('others', '項圈')], max_length=255, verbose_name='項目')),
                ('price', models.IntegerField(verbose_name='金額')),
            ],
            options={
                'verbose_name': '記帳',
                'verbose_name_plural': '記帳',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名稱')),
                ('gender', models.CharField(choices=[('male', '公'), ('female', '母')], default='請選擇', max_length=10, verbose_name='性別')),
                ('description', models.TextField(verbose_name='特徵')),
                ('species', models.CharField(choices=[('Bulldog', '鬥牛犬'), ('Corgi', '柯基'), ('Chihuahua', '吉娃娃'), ('Dachshund', '臘腸狗'), ('Golden', '黃金獵犬'), ('Labrador', '拉布拉多'), ('Maltese', '馬爾濟斯'), ('Pomeranian', '博美'), ('Poodle', '貴賓犬'), ('Husky', '哈士奇'), ('Terrier', '約克夏'), ('Schnauzer', '雪納瑞')], default='請選擇', max_length=10, verbose_name='品種')),
            ],
            options={
                'verbose_name': '寵物',
                'verbose_name_plural': '寵物',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('user_pwd', models.CharField(max_length=15)),
                ('check_password', models.CharField(max_length=15)),
                ('user_email', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '註冊',
                'verbose_name_plural': '註冊',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_url', models.CharField(default='', max_length=255, verbose_name='圖片網址')),
                ('shop_title', models.CharField(max_length=255, verbose_name='標題')),
                ('shop_price', models.CharField(max_length=20, verbose_name='價格')),
            ],
            options={
                'verbose_name': '商店',
                'verbose_name_plural': '商店',
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
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pwd', models.CharField(max_length=15)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.register')),
            ],
            options={
                'verbose_name': '登入',
                'verbose_name_plural': '登入',
            },
        ),
    ]
