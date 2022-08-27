from django.shortcuts import render, redirect
from django.http import HttpResponse

  
from .models import Adopciones

from .forms import AdopcionesForm

def inicio(request):
    return render(request, 'paginas/inicio.html')


def galeria(request): 
    galeria = Adopciones.objects.all()                                   #visualizar formulario en pagina 
    return render(request,'paginas/galeria.html', {'galeria': galeria})  #visualizar formulario en pagina 
    

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def publicar(request):
    return render(request, 'paginas/publicar.html')



def editar(request,id):
    adopcion = Adopciones.objects.get(id=id)
    formulario = AdopcionesForm(request.POST or None, request.FILES or None, instance=adopcion)
    if formulario.is_valid() and request.POST:   #para editar post
        formulario.save()                        #para editar post
        return redirect('galeria')               #para editar post
    return render(request,'contenido/editar.html', {'formulario': formulario})
    



def formulario(request):
    formulario = AdopcionesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('galeria')
    return render(request,'contenido/form.html', {'formulario': formulario})



def index(request):
    return render(request, 'contenido/index.html')



