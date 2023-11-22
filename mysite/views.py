from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
def showpost(request, slug):
    try:  
        post = Post.objects.get(slug = slug) 
        if post != None:
            return render(request, 'post.html',locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
    #select* from post where slug = %slug
    return render(request, 'post.html', locals())

import random
def about(request, num = -1):
    quotes = ["今日事，今日畢","失敗為成功之母","有志者，事竟成","一日之計在於晨"]
    if num == -1 or num >4:
        quote = random.choice(quotes)
    else:
        quote = quotes[num]
    
    return render(request, 'about.html', locals())

def carlist(request, maker=0):
	car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
	car_list = [ [],
	['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
	['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
	['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
	['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
	['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
	]
	maker = maker
	maker_name =  car_maker[maker]
	cars = car_list[maker]
	return render(request, 'carlist.html', locals())

    
'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append(f'No. {count} - {post} <br>')
        return HttpResponse(post_lists)
'''