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
    # http://127.0.0.1:8000/polls/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # http://127.0.0.1:8000/polls/1/results/
    path('<int:question_id>/results/', views.results, name='result'),
    # http://127.0.0.1:8000/polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
