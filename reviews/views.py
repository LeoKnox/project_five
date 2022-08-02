from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = "user"
    return render(request, "base.html", {"name":name})