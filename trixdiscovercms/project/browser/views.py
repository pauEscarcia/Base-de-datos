from django.http import HttpResponse
from models import Category
import datetime
from django.db.models import Q
from django.shortcuts import render_to_response


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


 
def latest_category(request):
    #category_list = Category.objects.order_by('name')[:1]
    category_list = Category.objects.order_by('name')
    return render_to_response('latest_category.html', {'category_list': category_list})

def latest_category1(request):
    #category_list = Category.objects.order_by('name')[:1]
    category_list = Category.objects.order_by('name')[:3]
    return render_to_response('latest_category.html', {'category_list': category_list})


