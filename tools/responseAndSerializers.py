import json
from django.core import serializers
from django.http import JsonResponse


def changeToResponse(data):
    serializer_data = serializers.serialize('json', data)
    json_data = json.loads(serializer_data)
    return JsonResponse(json_data, safe=False)
