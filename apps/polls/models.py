from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
# 模型1：问题
class Question(models.Model):
    # 显示对应字段的名称
    question_text = models.CharField(max_length=200, verbose_name="问题描述")
    # pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField(verbose_name="创建时间")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name_plural = '问题列表'


# 模型2：选项
class Choice(models.Model):
    # 外键，关联question的id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
