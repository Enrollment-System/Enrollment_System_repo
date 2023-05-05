# Generated by Django 4.2 on 2023-05-05 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_remove_subject_sub_teachers_subject_sub_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='sub_teachers',
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_teachers',
            field=models.ManyToManyField(blank=True, null=True, to='students.teachers'),
        ),
    ]