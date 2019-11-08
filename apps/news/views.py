from django.shortcuts import render
from django.views.generic.base import View
from .models import Article, Reporter
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from tools import transToJson


# Create your views here.


def index(request):
    article = Article.objects.all()
    return transToJson.changeToResponse(article)


def create(request):
    r = Reporter(full_name='安倍')
    r.save()
    return transToJson.changeToResponse(str(r.id))


def show(request):
    article = Article.objects.order_by('headline')
    output = ','.join([a.headline for a in article])
    return HttpResponse(output)
