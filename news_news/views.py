
# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import News    
def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news':news})

def redirect_view(request):
    return render(request, 'base.html')