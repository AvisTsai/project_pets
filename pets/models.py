from django.db import models


# Create your models here.
class Roast(models.TextChoices):
    # enum = value, display
    LIGHT = 'Light', '極淺度烘焙'
    CINNAMON = 'Cinnamon', '淺度烘焙'
    MEDIUM = 'Medium', '中度烘焙'
    HIGH = 'High', '中度微深烘焙'
    CITY = 'City', '中深度烘焙'
    FULL_CITY = 'Full-City', '微深度烘焙'
    FRENCH = 'French', '極深烘焙'
    ITALIAN = 'Italian', '極深度烘焙'


class OriginPlace(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '產地'
        verbose_name_plural = '產地'


class Tag(models.Model):
    name = models.CharField('名稱', max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'


class Pet(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)
    description = models.TextField('描述')
    roast = models.CharField('尺寸', max_length=10, choices=Roast.choices)
    price = models.PositiveIntegerField('價格')
    origin_place = models.ForeignKey(
        OriginPlace,
        on_delete=models.PROTECT,
        verbose_name='種類',
    )
    tags = models.ManyToManyField(Tag, verbose_name='標籤')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '咖啡豆'
        verbose_name_plural = '咖啡豆'

class MemberManagement(models.Model):
    UserID = models.CharField('使用者ID', max_length=20, unique=True)
    UserName = models.CharField('使用者名稱', max_length=20, unique=True)
    UserAccount = models.CharField('使用者帳號', max_length=20, unique=True)
    UserPassword = models.CharField('使用者密碼', max_length=20, unique=True)
    Email = models.CharField('使用者電子郵件', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '會員管理'
        verbose_name_plural = '會員管理'