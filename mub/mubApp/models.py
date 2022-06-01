from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=30)
    description = models.TextField(default="function was nice")
    thumbnail = models.ImageField(upload_to='event_images/')

class EventPhotos(models.Model):
    event = models.ForeignKey(Event , on_delete=models.CASCADE)
    event_photo = models.FileField(upload_to='event_images/')

class TrustMember(models.Model):
    name = models.CharField(max_length=100)
    occupation =models.CharField(max_length=30 ,blank = True)
    contribution = models.TextField(blank = True)

class JobSeeker(models.Model):
    GENDER_DEFAULT='S'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = (
        (GENDER_DEFAULT , 'Select Gender'),
        (GENDER_MALE, 'Male', ), 
        (GENDER_FEMALE, 'Female', ), 
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveBigIntegerField()
    area_of_work = models.CharField(max_length=100)
    highest_qualification = models.CharField(max_length=10)
    primary_skills = models.CharField(max_length=200)
    secondary_skills = models.CharField(max_length=200 , blank = True)
    experience = models.PositiveIntegerField()
    current_city = models.CharField(max_length=20)
    upload_resume = models.FileField(upload_to='resume/',blank = True)

class Directory(models.Model):
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photo/',blank = True)
    contact = models.CharField(max_length=10,primary_key=True)
    residence_address = models.TextField(blank = True)
    business_address = models.TextField(blank = True)

class Matrimonial(models.Model):
    GENDER_DEFAULT='S'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = (
        (GENDER_DEFAULT , 'Select Gender'),
        (GENDER_MALE, 'Male', ), 
        (GENDER_FEMALE, 'Female', ), 
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank = True)
    contact = models.CharField(max_length=10 , primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveBigIntegerField()
    describe_yourself = models.TextField(blank = True)
    profile_photo = models.ImageField(upload_to='profile_photo/',blank = True)
    upload_bio_data = models.FileField(upload_to='bio_data/',blank = True)


class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    url = models.URLField(blank = True)
    description = models.TextField(blank = True)

class Sponsor(models.Model):
    title = models.CharField(max_length=100)