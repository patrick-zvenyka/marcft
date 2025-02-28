from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def home(request):
    return render (request, 'index.html', {'title':'Marcft - Home'})

def team(request):
    return render(request, 'team.html', {'title':'Marcft - Our Team'})

def services(request):
    return render(request, 'services.html', {'title':'Marcft - Our Activities'})

def about(request):
    return render(request, 'about.html', {'title':'Marcft - About Us'})

def contact(request):
    return render(request, 'contact.html', {'title':'Marcft - Contact Us'})


def blog(request):
   
    posts = Post.objects.all().order_by('-created_at')

    op_obj = Post.objects.count()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'posts' : posts,
        'op_obj': op_obj,
        'data':data,
        'title':'Marcft - Updates',
    }
    return render(request, 'blog.html', context)

def singleblog(request, id):
    post = Post.objects.get(id=id)
    context = {
        
        'post' : post,
        'title':'Marcft - Update'
       
    }

    return render(request, 'blog-single.html', context)

