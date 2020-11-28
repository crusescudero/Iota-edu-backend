from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import CoursesViewSet

router = routers.DefaultRouter()
router.register('coursesApi',CoursesViewSet)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('login/', views.loginview, name='loginview'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('done/', auth_views.PasswordResetCompleteView.as_view(template_name='done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    
    path('reset_confirmed/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_confirmed.html'),
    name='password_reset_complete'),

    path('api/',include(router.urls)),
    
]
