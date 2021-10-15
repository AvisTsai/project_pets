import django
from django.utils import timezone

from django.urls import reverse
from django.db import models


# 註冊
class Register(models.Model):
    username = models.CharField(max_length=15)
    user_pwd = models.CharField(max_length=15)
    check_password = models.CharField( max_length=15)
    user_email = models.CharField( max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '註冊'
        verbose_name_plural = '註冊'


# Create your models here.
class Species(models.TextChoices):
    # enum = value, display
    Bulldog = 'Bulldog', '鬥牛犬'
    Corgi = 'Corgi', '柯基'
    Chihuahua = 'Chihuahua', '吉娃娃'
    Dachshund = 'Dachshund', '臘腸狗'
    Golden = 'Golden', '黃金獵犬'
    Labrador = 'Labrador', '拉布拉多'
    Maltese = 'Maltese', '馬爾濟斯'
    Pomeranian = 'Pomeranian', '博美'
    Poodle = 'Poodle', '貴賓犬'
    Husky = 'Husky', '哈士奇'
    Terrier = 'Terrier', '約克夏'
    Schnauzer = 'Schnauzer', '雪納瑞'


class Gender(models.TextChoices):
    male = 'male', '公'
    female = 'female', '母'


# class OriginPlace(models.Model):
#     name = models.CharField('名稱', max_length=20, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = '寵物'
#         verbose_name_plural = '寵物'


class Tag(models.Model):
    name = models.CharField('名稱', max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'


class Pet(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)
    gender = models.CharField('性別', max_length=10, choices=Gender.choices, default='請選擇')
    description = models.TextField('特徵')
    species = models.CharField('品種', max_length=10, choices=Species.choices, default='請選擇')

    # price = models.PositiveIntegerField('價格')
    # origin_place = models.ForeignKey(
    #     OriginPlace,
    #     on_delete=models.PROTECT,
    #     verbose_name='種類',
    # )
    # tags = models.ManyToManyField(Tag, verbose_name='標籤')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '寵物'
        verbose_name_plural = '寵物'


class MemberManagement(models.Model):
    UserID = models.CharField('使用者ID', max_length=20, unique=True)
    UserName = models.CharField('使用者名稱', max_length=20, unique=True)
    UserAccount = models.CharField('使用者帳號', max_length=20, unique=True)
    UserPassword = models.CharField('使用者密碼', max_length=20, unique=True)
    Email = models.CharField('使用者電子郵件', max_length=20, unique=True)

    def __str__(self):
        return self.UserName

    class Meta:
        verbose_name = '會員管理'
        verbose_name_plural = '會員管理'


# 記帳

class Category(models.TextChoices):
    food = 'food', '食物'
    toy = 'toy', '玩具'
    clothes = 'clothes', '衣服'
    salon = 'salon', '美容'
    others = 'others', '其他'


class Money(models.Model):
    time = models.DateTimeField(default=django.utils.timezone.now)
    category = models.CharField(max_length=255, choices=Category.choices, default='未分類')
    item = models.CharField(max_length=255, verbose_name='項目')
    price = models.IntegerField(default=0, verbose_name='金額')

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = '記帳'
        verbose_name_plural = '記帳'

#         行事曆

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
# Create your models here.
# 創造model
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
