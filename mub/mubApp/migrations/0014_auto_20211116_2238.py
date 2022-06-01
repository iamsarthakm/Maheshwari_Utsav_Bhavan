# Generated by Django 3.2.6 on 2021-11-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubApp', '0013_auto_20211116_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matrimonial',
            name='looking_for',
        ),
        migrations.AddField(
            model_name='matrimonial',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='profile_photo/'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_one',
            field=models.ImageField(upload_to='event_images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='event_images/'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='secondary_skills',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='upload_resume',
            field=models.FileField(blank=True, upload_to='resume/'),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='describe_yourself',
            field=models.TextField(blank=True, default='Describe youself'),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='upload_bio_data',
            field=models.FileField(blank=True, upload_to='bio_data/'),
        ),
        migrations.AlterField(
            model_name='trustmember',
            name='contribution',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trustmember',
            name='occupation',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]