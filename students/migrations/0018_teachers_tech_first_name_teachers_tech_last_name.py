# Generated by Django 4.2 on 2023-05-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_alter_academicyear_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='tech_first_name',
            field=models.CharField(default='adf', max_length=50),
        ),
        migrations.AddField(
            model_name='teachers',
            name='tech_last_name',
            field=models.CharField(default='adfad', max_length=50),
        ),
    ]