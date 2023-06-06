import requests
from django.http import JsonResponse
from django.shortcuts import render
import json


Response = requests.get('https://jsonplaceholder.typicode.com/todos').json()


def todo(request):
    return JsonResponse({'todo list': Response})


def home(request):
    return render(request, 'home.html')




