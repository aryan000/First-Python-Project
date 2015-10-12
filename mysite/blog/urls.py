"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns , include ,url
from django.views.generic import ListView ,DetailView
from blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(
    	queryset=Post.objects.all().order_by("-date")[:10],
    	template_name="blog.html"))	,

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
    	model = Post,
    	template_name="post.html"))	, 

    url(r'^archives/$', ListView.as_view(
    	queryset=Post.objects.all().order_by("-date"),
    	template_name="posttitleslist.html"))	,

    url(r'^latestnews$', ListView.as_view(
    	queryset=Post.objects.all().order_by("-date")[:5],
    	template_name="latestnews.html"))	,




]
