import json
from django.shortcuts import render
from django.db import connection, connections
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .models import Book
from tools import transToJson


# Create your views here.
def bookDetail(request):
    # sql = "SELECT * FROM bookstore_book WHERE book_name=%s"
    sql = "SELECT * FROM bookstore_book"
    return transToJson.toJsonResponse(sql)
    # cursor.execute(sql, ['朝花夕拾'])
    # 调用存储过程
    #     # cursor.callproc('test_procedure', [1, 'test'])
    # book = cursor.fetchall()

    # json_book = serializers.serialize('json', book)
    # json_book = json.dumps(book, cls=transToJson.DateEncoder)
    # json_book = json.loads(json_book)
    # return JsonResponse(json_book, safe=False)
    # return HttpResponse("<h1>" + str(list(b)) + "</h1>")
    # book = Book.objects.all()
    # json_book = serializers.serialize('json', book)
    # json_book = json.loads(json_book)
    # return JsonResponse(json_book, safe=False)


def otherDB(request):
    # with connections['mxshop'].cursor() as cursor:
    sql = 'SELECT * FROM goods_goods LIMIT 10'
    return transToJson.toJsonResponse(sql, database='mxshop')
    #     cursor.execute(sql)
    #     b = cursor.fetchone()
    # # return responseAndSerializers.changeToResponse(b)
    # return HttpResponse("<h1>" + str(list(b)) + "</h1>")


def testTools(request):
    books = Book.objects.all()
    # books = 123
    return transToJson.toJsonResponse(books)
