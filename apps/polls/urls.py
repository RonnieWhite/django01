"""
@author     ：bai.chenghui
@date       ：Created in 2019/10/8 10:17
@description：
@modified By：
@version:     
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test1', views.test1, name='test1'),
    path('test2', views.test2, name='test2'),
    path('test3', views.test3, name='test3'),
]
