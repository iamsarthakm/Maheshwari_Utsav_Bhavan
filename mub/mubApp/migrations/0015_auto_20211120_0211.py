# Generated by Django 3.2.6 on 2021-11-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubApp', '0014_auto_20211116_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonial',
            name='describe_yourself',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='gender',
            field=models.CharField(choices=[('S', 'Select Gender'), ('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
