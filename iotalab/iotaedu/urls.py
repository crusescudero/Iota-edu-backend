from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('login/', views.loginview, name='loginview'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]