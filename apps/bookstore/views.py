from django.shortcuts import render
from django.db import connection, connections
from django.http import HttpResponse
from tools import responseAndSerializers


# Create your views here.
def bookDetail(request):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM bookstore_book WHERE book_name=%s"
        cursor.execute(sql, ['朝花夕拾'])
        # 调用存储过程
        # cursor.callproc('test_procedure', [1, 'test'])
        b = cursor.fetchone()
    return HttpResponse("<h1>" + str(list(b)) + "</h1>")


def otherDB(request):
    with connections['mxshop'].cursor() as cursor:
        sql = 'select * from goods_goods'
        cursor.execute(sql)
        b = cursor.fetchone()
    # return responseAndSerializers.changeToResponse(b)
    return HttpResponse("<h1>" + str(list(b)) + "</h1>")
