# Generated by Django 3.1.3 on 2020-11-06 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotaedu', '0004_auto_20201105_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_url',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
