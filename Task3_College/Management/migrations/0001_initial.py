# Generated by Django 3.2.7 on 2021-09-12 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=32)),
                ('Subject', models.CharField(max_length=32)),
                ('Department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Management.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.IntegerField()),
                ('Name', models.CharField(max_length=32)),
                ('Address', models.CharField(max_length=50)),
                ('Department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Management.departments')),
            ],
        ),
    ]
