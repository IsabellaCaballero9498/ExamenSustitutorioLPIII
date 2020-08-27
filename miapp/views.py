from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Libro

def inicio(request):
    return render(request,'inicio.html',{
        'titulo': 'Inicio',
    })


def listar_libro(request):
    libros = Libro.objects.all()    
    return render(request,'libro.html',{
        'libros': libros,
        'titulo': 'libros'
    })

def eliminar_libro(request, id):
    libro = Libro.objects.get(pk=id)
    libro.delete()
    return redirect('listar_libro')