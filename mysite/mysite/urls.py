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
from django.conf.urls import include, url
from django.contrib import admin 
from blog.views import HelloTemplate
admin.autodiscover()

urlpatterns = [
    url(r'^hello/$',  'blog.views.hello'), 
    url(r'^hello_template/$',  'blog.views.hello_template'), 
    url(r'^hello_template_simple/$',  'blog.views.hello_template_simple'), 
    url(r'^hello_class_view/$', HelloTemplate.as_view()), 
    url(r'^', include('blog.urls')), 
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
