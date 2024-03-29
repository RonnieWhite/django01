# Generated by Django 2.2.6 on 2019-11-06 22:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('full_name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=1, verbose_name='性别')),
                ('country', models.CharField(default='', max_length=50, verbose_name='国籍')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('book_name', models.CharField(max_length=50, verbose_name='书名')),
                ('shop_price', models.FloatField(default=0.0, verbose_name='价格')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Author', verbose_name='作者')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
