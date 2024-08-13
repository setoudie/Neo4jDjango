from .models import Prompt, Owner
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# My first test view in django
def index(request):
    return HttpResponse("<h1>Ceci est un test</h1>")

# Another test view
def test(request):
    return HttpResponse('<li> Test 1 </li>')

# Route pour creer un prompt
def create_prompt(request):
    if request.method == 'POST':
        data = request.POST
        owner_username = data.get('owner_username')
        owner = Owner.nodes.get(username=owner_username)
        prompt = Prompt(content=data['content']).save()
        prompt.owner.connect(owner)
        # return redirect('index', prompt_id=prompt.pid)
    return render(request, 'prompts/create_prompt.html')

def update_prompt(request, prompt_id):
    prompt = Prompt.nodes.get(pid=prompt_id)

    print(prompt_id)
    print(f"\n\n {prompt}")

    if request.method == 'POST':
        data = request.POST
        prompt.content = data.get('content', prompt.content)
        prompt.save()
    return render(request, 'prompts/update_prompt.html', {'prompt': prompt})

def delete_prompt(request, prompt_id):
    prompt = Prompt.nodes.get(pid=prompt_id)
    if request.method == 'POST':
        prompt.delete()
        return redirect('create_prompt')
    return render(request, 'prompts/delete_prompt.html', {'prompt': prompt})

