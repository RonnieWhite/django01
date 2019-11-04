"""
@author     ：bai.chenghui
@date       ：Created in 2019/10/8 10:17
@description：
@modified By：
@version:     
"""
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path('', views.index, name='index'),
]
