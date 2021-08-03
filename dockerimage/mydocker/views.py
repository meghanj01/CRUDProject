from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render ,HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1> 'Hello, Docker!'</h1>")