from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# My first test view in django
def index(request):
    return HttpResponse("<h1>Ceci est un test</h1>")

# Another test view
def test(request):
    return HttpResponse('<li> Test 1 </li>')