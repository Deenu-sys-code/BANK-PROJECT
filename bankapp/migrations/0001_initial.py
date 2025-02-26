# Generated by Django 5.1.3 on 2024-12-28 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ac_num', models.BigIntegerField(unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Email_id', models.EmailField(max_length=254)),
                ('Ph_number', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Statements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('History', models.CharField(max_length=50)),
                ('Date', models.DateField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Statement', to='bankapp.customer')),
            ],
        ),
    ]
