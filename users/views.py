from django.shortcuts import render
from  django.http import HttpResponse
from django.template import loader

# Create your views here.
# Login View
def login(request):
    temp = loader.get_template("users/login.html")
    return HttpResponse(temp.render())

def test(request):
    # temp = loader.get_template("users/login.html")
    return HttpResponse('<h1>Test</h1>')