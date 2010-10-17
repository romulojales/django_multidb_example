# Create your views here.
from django.http import HttpResponse
from models import Principal,Auxiliar
from random import random


def save_default(resquest):
    

    p=Principal(title=str(random()),author=str(random()))
    p.save()
    return HttpResponse("Salvo")

def save_auxiliar(request):
    p=Auxiliar(title=str(random()),author=str(random()))
    p.save()
    return HttpResponse("Salvo")

def all_default(request):
    html = "<html><body>Lista de principal<table border='1'>"
    html += "<tr><td>ID</td><td>Author</td><td>Title</td></tr>"
    for i in  Principal.objects.all():
        html+= "<tr><td>"+str(i.id)+"</td><td>"+i.author+"</td><td>"+i.title+"</td></tr>"
    html+="</table></body></html>"
    return HttpResponse(html)


def all_auxiliar(request):
    html = "<html><body>Lista de auxiliar<table border='1'>"
    html += "<tr><td>ID</td><td>Author</td><td>Title</td></tr>"
    for i in  Auxiliar.objects.all():
        html+= "<tr><td>"+str(i.id)+"</td><td>"+i.author+"</td><td>"+i.title+"</td></tr>"
    html+="</table></body></html>"
    return HttpResponse(html)
    return HttpResponse(html)
