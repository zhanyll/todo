from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")