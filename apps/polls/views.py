from datetime import datetime
import json
from django.http import HttpResponse, HttpResponseNotFound
from .models import Question
from django.core import serializers
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def test1(request):
    # foo = True
    # if foo:
    #     return HttpResponseNotFound('<h1>Page not found</h1>')
    # else:
    #     return HttpResponse('<h1>hello!</h1>')
    # question = Question.objects.raw("select id, question_text, pub_date from polls_question")[0]
    # question = Question.objects.all()[1:]
    # json_data = serializers.serialize('json', question)
    # json_data = json.loads(json_data)
    # return json_data
    # return JsonResponse(json_data, safe=False)
    # sql = "select id, question_text, pub_date from polls_question"
    # with connection.cursor() as cursor:
    #     cursor.execute(sql)
    #     row = cursor.fetchall()
    #     json_row = serializers.serialize('json', row)
    #     json_row = json.loads(json_row)
    #     return JsonResponse(json_row, safe=False)
    now = datetime.now()
    html = "<html5><body>It is now %s.</body></html5>" % now
    return HttpResponse(html)


def test2(request):
    question = Question.objects.all()
    json_question = serializers.serialize('json', question)
    json_question = json.loads(json_question)
    return JsonResponse(json_question, safe=False)


def test3(request):
    return render(request, "static/html5/detail.html")
