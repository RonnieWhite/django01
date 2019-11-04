from django.shortcuts import render
from django.views.generic.base import View
from .models import Article, Reporter
from django.core import serializers
from django.http import JsonResponse
from tools import responseAndSerializers


# Create your views here.


def index(request):
    article = Article.objects.all()
    return responseAndSerializers.changeToResponse(article)


def create(request):
    r = Reporter(full_name='安倍')
    r.save()
    return responseAndSerializers.changeToResponse(str(r.id))
