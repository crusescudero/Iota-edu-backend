# Generated by Django 3.1.3 on 2020-11-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotaedu', '0003_courses_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_image',
            field=models.ImageField(upload_to='iotaedu/static/assets/img'),
        ),
    ]
