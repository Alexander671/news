from django.shortcuts import render
from django.http import HttpResponse

def drafts(request):
    return HttpResponse("Ddrafts Page")