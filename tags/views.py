from django.shortcuts import render
from django.http import HttpResponse

def tags(request):
    return HttpResponse("Tags Page")