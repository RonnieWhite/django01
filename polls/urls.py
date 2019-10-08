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
]
