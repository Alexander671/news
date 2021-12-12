
# accounts/views.py

from django.http import HttpResponse
from django.shortcuts import render

from autors.models import Autors
def autors(request):
    autors = Autors.objects.all()
    return render(request, "autors/autors.html", {'autors' : autors})


def become_autor(request):
    return HttpResponse('Become Autor Page!')

