from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "to Bookr"
    return HttpResponse("Welcome {}!".format(name))