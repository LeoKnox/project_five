from django.shortcuts import render

def index(request):
    name = "user"
    return render(request, "base.html", {"name":name})