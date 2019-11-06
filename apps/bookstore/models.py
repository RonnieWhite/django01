from datetime import datetime
from django.db import models


# Create your models here.
class CommonInfo(models.Model):
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        abstract = True


class Author(CommonInfo):
    GENDER = [
        ('M', '男'),
        ('F', '女'),
    ]
    full_name = models.CharField(max_length=50, verbose_name='姓名')
    age = models.IntegerField(default=0, verbose_name='年龄')
    gender = models.CharField(default='M', max_length=1, choices=GENDER, verbose_name='性别')
    country = models.CharField(default='', max_length=50, verbose_name='国籍')

    class Meta:
        verbose_name = '作家'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.full_name


class Book(CommonInfo):
    book_name = models.CharField(max_length=50, verbose_name='书名')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
    shop_price = models.FloatField(default=0.0, verbose_name='价格')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name+'---'+str(self.shop_price)
