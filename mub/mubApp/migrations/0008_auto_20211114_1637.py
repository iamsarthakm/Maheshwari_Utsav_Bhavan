# Generated by Django 3.2.6 on 2021-11-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubApp', '0007_alter_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrimonial',
            name='bio_data',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
