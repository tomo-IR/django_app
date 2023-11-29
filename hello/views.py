from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request, nickname, age):
    result = 'your account: ' + nickname + '" (' + str(age) + ').'
    return HttpResponse(result)