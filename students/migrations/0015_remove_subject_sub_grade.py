# Generated by Django 4.2 on 2023-05-04 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_alter_subject_sub_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='sub_grade',
        ),
    ]
