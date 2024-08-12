from django.shortcuts import render
from A_Blog.models import Post, Categoria

# Create your views here.

def blog(request):
    posts=Post.objects.all()
    return render(request, 'A_Blog/blog.html', {'posts':posts})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, 'A_Blog/categoria.html', {'categoria':categoria, 'posts':posts})