from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("hello world")

def test(request):
    return render(request, "test.html")