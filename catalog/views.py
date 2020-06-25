from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home_view(request):
    now = datetime.datetime.now()
    html = "<html><body>Now is  %s.</body></html>" % now
    return HttpResponse(html)