from datetime import date
from django.db import models


# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70, verbose_name="记者全名")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = '记者'
        verbose_name_plural = verbose_name


class Article(models.Model):
    pub_date = models.DateField(verbose_name="发布时间")
    headline = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    reporter = models.ForeignKey(Reporter, verbose_name="作者", on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
