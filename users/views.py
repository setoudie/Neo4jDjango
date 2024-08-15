from django.shortcuts import render
from  django.http import HttpResponse
from django.template import loader

from prompt.models import Owner


# Create your views here.
# Login View
def login(request):
    temp = loader.get_template("users/login.html")
    return HttpResponse(temp.render())

def test(request):
    # temp = loader.get_template("users/login.html")
    return HttpResponse('<h1>Test</h1>')

# Create user
def create_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        # usernames = data.get('username')
        # print(usernames)
        owner = Owner(username=username)
        owner.save()

    return render(request, template_name='users/create_user.html')

