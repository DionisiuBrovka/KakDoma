from django.http import HttpResponse
from django.shortcuts import render
from data.models import News, Towns
import csv

# Create your views here.  
def index(request):
    data = {
        'news' : News.objects.all().order_by('-pub_date')[:5],
        'towns' : Towns.objects.all().order_by('-name')
    }
    return render(request, 'landing/index.html', data)

def news(request):
    data = {
        'news' : News.objects.all().order_by('-pub_date'),
        'towns' : Towns.objects.all().order_by('-name')
    }
    return render(request, 'news/index.html', data)