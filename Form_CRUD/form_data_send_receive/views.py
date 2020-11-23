from django.http import JsonResponse, Http404, HttpResponse
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


@csrf_exempt
def PersonView(request,id):

    try:
        persondetails = Form.objects.get(pk=id)

    except Form.DoesNotExist:
        return Http404

    if request.method == 'GET':
        SerializeData = FormSerializer(persondetails)
        return JsonResponse(SerializeData.data,safe=False)

    elif request.method == 'POST':
        raw_data = json.dumps(request.POST)
        data = json.loads(raw_data)
        modified_data = FormSerializer(persondetails,data=data)
        if modified_data.is_valid():
            modified_data.save()
        return HttpResponse(status=200)


@csrf_exempt
def Persondelete(request,id):

    try:
        persondetails = Form.objects.get(pk=id)

    except Form.DoesNotExist:
        return Http404

    if request.method == 'POST':
        persondetails.delete()
        return HttpResponse(status=200)
