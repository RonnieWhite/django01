import json
import datetime
from django.core import serializers
from django.http import JsonResponse
from django.db import connections


# 转换Django的QuerySet API结果为JsonResponse
def QSToJR(data):
    try:
        serializer_data = serializers.serialize('json', data)
        json_data = json.loads(serializer_data)
    except TypeError:
        json_data = str(data) + '-----param error, show be Django QuerySet'
    return JsonResponse(json_data, safe=False)


# 转换原生SQL查询的结果为JsonResponse
def toJsonResponse(sql, database='default'):
    with connections[database].cursor() as cursor:
        cursor.execute(sql)
        desc = cursor.description
        data = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
    return JsonResponse(data, safe=False)


# 重写json的JSONEncoder类，用以转换时间类型数据为json
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)
