from django.http import HttpResponse
from django.shortcuts import render
from data.models import News

# Create your views here.  
def index(request):
    data = {
        'news' : News.objects.all().order_by('-pub_date')[:5]
    }

    return render(request, 'landing/index.html', data)