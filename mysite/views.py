from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
def showpost(request, slug):
    post = Post.objects.get(slug = slug) 
    #select* from post where slug = %slug
    return render(request, 'post.html', locals())



'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append(f'No. {count} - {post} <br>')
        return HttpResponse(post_lists)
'''