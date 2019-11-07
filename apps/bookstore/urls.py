"""
@author     ：bai.chenghui
@date       ：Created in 2019/10/8 10:17
@description：
@modified By：
@version:
"""
from django.urls import path
from . import views

app_name = 'bookstore'
urlpatterns = [
    # http://127.0.0.1:8000/bookstore/bookDetail
    path('bookDetail', views.bookDetail, name='bookDetail'),
    path('otherDB', views.otherDB, name='otherDB'),
]
