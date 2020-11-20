# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser, MultiPartParser,FormParser
import json

from .models import *
from .serializer import FormSerializer

# Create your views here.


@csrf_exempt
def FormView(request):

    if request.method == 'GET':
        data = Form.objects.all()
        SerializeData = FormSerializer(data,many=True)
        return JsonResponse(SerializeData.data,safe=False)

    elif request.method == 'POST':
        raw_data = json.dumps(request.POST)
        data = json.loads(raw_data)
        SerializeData = FormSerializer(data=data)
        if SerializeData.is_valid():
            SerializeData.save()
            data = Form.objects.all()
            SerializeData = FormSerializer(data, many=True)
            return JsonResponse(SerializeData.data, safe=False)
        return JsonResponse(SerializeData.errors,status=400)