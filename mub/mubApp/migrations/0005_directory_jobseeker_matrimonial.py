# Generated by Django 3.2.6 on 2021-11-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubApp', '0004_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.PositiveBigIntegerField()),
                ('occupation', models.CharField(max_length=100)),
                ('current_city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.PositiveBigIntegerField()),
                ('area_of_work', models.CharField(max_length=100)),
                ('primary_skills', models.CharField(max_length=200)),
                ('secondary_skills', models.CharField(max_length=200)),
                ('experience', models.PositiveIntegerField()),
                ('current_city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Matrimonial',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.PositiveBigIntegerField()),
                ('describe_yourself', models.TextField(default='Describe youself')),
                ('looking_for', models.TextField(default='Describe what are you looking for in your life partner')),
            ],
        ),
    ]
