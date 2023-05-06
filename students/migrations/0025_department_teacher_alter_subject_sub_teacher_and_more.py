# Generated by Django 4.2 on 2023-05-06 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_alter_academicyear_subject1_alter_subject_sub_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('dep_n', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_first_name', models.CharField(max_length=50)),
                ('tech_last_name', models.CharField(max_length=50)),
                ('tech_email', models.EmailField(max_length=50)),
                ('tec_dob', models.DateField()),
                ('tech_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.department')),
            ],
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.teacher'),
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]