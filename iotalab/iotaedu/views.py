from .models import Courses
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from iotaedu.forms import ContactForm, CreateUser, LoginUserForm


from django.contrib import messages

# rest_framework
from rest_framework import status
from rest_framework import viewsets
from .serializers import CoursesSerializer


# API uptake
from urllib.request import urlopen 
import json
import urllib.request

# Create your views here.

def index(request):
    
    title = "Home"
    valores = ["UF", "UTM", "USD"]

    context = {
        'title': title
    }

    for codigo in valores:
        url = "https://api.gael.cl/general/public/monedas/{}".format(codigo)
        datos = urllib.request.urlopen(url).read()
        moneda = json.loads(datos)
        valorMoneda = moneda["Valor"]

        context[codigo] = valorMoneda
    print(context)

    return render(request, 'home.html', context)

    
    


# Vista de cursos
def courses(request):
    title = "Cursos" 
    getCoursesList = Courses.objects.order_by('course_name')

    for course in getCoursesList:
        course.course_image = str(course.course_image).replace('iotaedu/static/', '')

    context = {
        'title': title,
        'getCoursesList': getCoursesList, 
    }

    return render(request, 'courses.html', context)

# Vista de nosotros
def about(request):
    title = "Nosotros"
    context = {
        'title': title
    }
    return render(request, 'about.html', context)

# Vista de contacto
def contact(request):
    form = ContactForm()
    title = "Contacto"
    context = {
        'title': title,
        'form': form
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Nombre']
            email = form.cleaned_data['Email']
            phone = form.cleaned_data['Telefono']
            message = form.cleaned_data['Mensaje']

            mail_txt = 'Nuevo contacto! nombre: {0}, telefono: {1}, correo: {2}, ha escrito el siguiente mensaje: {3}'.format(name, phone, email, message)

            send_mail(
                'Nuevo mensaje - IotaEducation',
                mail_txt,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

    return render(request, 'contact.html', context)

# Vista crear usuarios
def register(request):
    form = CreateUser()
    title = 'Registro'
    context = {
        'title': title,
        'form': form
    }

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            username = form.cleaned_data['Nombre']
            password = form.cleaned_data['Contraseña']

            User.objects.create_user(username, email, password)
            return redirect('/')
    return render(request, 'register.html', context)

# login view
def loginview(request):
    form = LoginUserForm()
    title = 'Login'
    context = {
        'title': title,
        'form': form
    }

    if request.method == 'POST':

        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Usuario o contraseña incorrecta')
            

    return render(request, 'login.html', context)

# función de cerrar sesión
def logoutUser(request):
    logout(request)
    return redirect('/')

# clase de consulta 
class CoursesViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer