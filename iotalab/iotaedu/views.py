from django.shortcuts import render
from django.http import HttpResponse

from .models import Courses

# Create your views here.
def index(request):
    title = "Home"
    return render(request, 'home.html', {
        'title': title,
    })

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

def about(request):
    title = "Nosotros"
    return render(request, 'about.html')


def contact(request):
    title = "Contacto"
    return render(request, 'contact.html')