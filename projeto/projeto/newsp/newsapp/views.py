from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image 
import os
from django.conf import settings
from datetime import date 

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "pagina1.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        
        img = Image.open(file)
        path = os.path.join(settings.BASE_DIR, f'media/{file.name}-{date.today()}.png')
        img = img.save(path)


        print(file)

        return HttpResponse('teste')

def cadastro(request):
    return render(request, "cadastro/cadastro.html")

def login(request):
    return render(request, "login.html")