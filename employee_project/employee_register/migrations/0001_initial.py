# Generated by Django 4.0.1 on 2023-11-20 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('ecode', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=10)),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.roles')),
            ],
        ),
    ]
