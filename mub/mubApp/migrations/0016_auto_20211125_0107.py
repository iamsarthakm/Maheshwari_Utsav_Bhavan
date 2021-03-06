# Generated by Django 3.2.6 on 2021-11-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubApp', '0015_auto_20211120_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='venue',
        ),
        migrations.RemoveField(
            model_name='directory',
            name='age',
        ),
        migrations.RemoveField(
            model_name='directory',
            name='current_city',
        ),
        migrations.RemoveField(
            model_name='directory',
            name='email',
        ),
        migrations.RemoveField(
            model_name='directory',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='directory',
            name='occupation',
        ),
        migrations.AddField(
            model_name='directory',
            name='business_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='directory',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='profile_photo/'),
        ),
        migrations.AddField(
            model_name='directory',
            name='residence_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='highest_qualification',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='directory',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('S', 'Select Gender'), ('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trustmember',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
