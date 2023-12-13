"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as siteviews
from mytest import views as testviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', siteviews.homepage, name="homepage"),
    path('post/<slug:slug>/', siteviews.showpost, name="showpost"),
    path('post/', siteviews.show_all_posts, name="show-all-posts"),
    path('post/<int:post_id>/comments', siteviews.show_comments, name='show-comments'),
    path('about/', siteviews.about),
    path('about/<int:num>', siteviews.about, name='about'),
    path('carlist/', siteviews.carlist),
    path('carlist/<int:maker>/', siteviews.carlist, name='carlist-url'),
    path('post/new', siteviews.new_post, name="post-new"),
    path('test/', testviews.index, name="test-new")
]
