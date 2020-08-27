from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Libro,Autor,Editorial,Pais

def inicio(request):
    return render(request,'inicio.html',{
        'titulo': 'Inicio',
    })


def listar_libro(request):
    libros = Libro.objects.all()    
    return render(request,'libro.html',{
        'libros': libros,
        'titulo': 'Listado de libros'
    })

def eliminar_libro(request, id):
    libro = Libro.objects.get(pk=id)
    libro.delete()
    return redirect('listar_libro')

def listar_autor(request):
    autores = Autor.objects.all()    
    return render(request,'autores.html',{
        'autores': autores,
        'titulo': 'Listado de autores'
    })

def eliminar_autor(request, id):
    autor = Autor.objects.get(pk=id)
    autor.delete()
    return redirect('listar_autor')


def listar_editorial(request):
    editoriales = Editorial.objects.all()    
    return render(request,'editorial.html',{
        'editoriales': editoriales,
        'titulo': 'Listado de editoriales'
    })

def eliminar_editorial(request, id):
    editorial = Editorial.objects.get(pk=id)
    editorial.delete()
    return redirect('listar_editorial')


def listar_pais(request):
    paises = Pais.objects.all()    
    return render(request,'pais.html',{
        'paises': paises,
        'titulo': 'Listado de paises'
    })

def eliminar_pais(request, id):
    pais = Pais.objects.get(pk=id)
    pais.delete()
    return redirect('listar_pais')

def consultas(request):
    return render(request,'consultas.html',{
        'titulo': 'Consultas y comentarios',
    })

