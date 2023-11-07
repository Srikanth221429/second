from django.shortcuts import render
from django.http import HttpResponse
from app.views import *

# Create your views here.
def fun(request):
    return HttpResponse("Hii ")
