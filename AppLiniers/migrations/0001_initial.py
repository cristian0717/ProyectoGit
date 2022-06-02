# Generated by Django 4.0.4 on 2022-06-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('puesto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Delantero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('puesto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('puesto', models.IntegerField()),
            ],
        ),
    ]
