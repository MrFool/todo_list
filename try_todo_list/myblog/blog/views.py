from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html',{'wenzhangs': articles})