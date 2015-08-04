"""RentIt URL Configuration

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
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^$', 'RentItApp.home_views.home', name='home'),
                       url(r'^login', 'RentItApp.login_views.login', name='login'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^register', 'RentItApp.views.register', name='register'),
                       url(r'^show', 'RentItApp.views.show', name='show'),
                       url(r'^edit', 'RentItApp.views.show_details', name='show_details'),
                       url(r'^product_add', 'RentItApp.product_views.product_add', name='product_add'),
                       url(r'^product_data_add', 'RentItApp.product_views.product_data_add', name='product_data_add'),
                       url(r'upload_product_image', 'RentItApp.product_views.upload_product_image',
                           name='upload_product_image')
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
