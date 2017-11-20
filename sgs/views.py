from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>In index view</p>')

def shipment_detail(request, id):
    return HttpResponse('<p>In shipment_detail view with id {0}</p>'.format(id))

def upload_detail(request, id):
    return HttpResponse('<p>In upload_detail view with id {0}</p>'.format(id))
