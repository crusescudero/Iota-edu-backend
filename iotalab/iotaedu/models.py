from django.db import models

# Create your models here.
class Courses(models.Model):
  course_name = models.CharField(max_length=100)
  course_price = models.IntegerField(default=0)
  course_nextDate = models.CharField(max_length=150)
  course_materials = models.CharField(max_length=300)
  course_objectives = models.CharField(max_length=300)
  course_description = models.CharField(max_length=300)
  course_image = models.ImageField(upload_to='iotaedu/static/assets/img')
  course_url = models.CharField(max_length=500)