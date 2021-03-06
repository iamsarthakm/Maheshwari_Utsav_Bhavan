# Generated by Django 3.2.6 on 2021-11-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubApp', '0009_auto_20211114_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
