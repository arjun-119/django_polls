from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello!, This is the polls index!")

def test(request):
    return HttpResponse("Test")