# Generated by Django 4.2 on 2023-05-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_academicyear_subject1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicyear',
            name='subject1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='subject2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='subject3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='subject4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='subject5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='subject6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
