from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from mubApp.models import JobSeeker, Event, Matrimonial, Directory, TrustMember, Ad, Sponsor, Admin  , EventPhotos
from django.contrib.auth import login
from django.forms.widgets import PasswordInput, TextInput


# class CustomAuthForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(
#         widget=PasswordInput(attrs={'class': 'form-control'}))


class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class JobSeekerForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=JobSeeker.GENDER_CHOICES , widget=forms.Select(attrs={ 'class': 'form-control'}))

    class Meta:
        model = JobSeeker
        fields = ('name', 'email', 'contact', 'gender', 'age','highest_qualification','area_of_work',
                  'primary_skills', 'secondary_skills', 'experience', 'current_city', 'upload_resume')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'highest_qualification':forms.TextInput(attrs={'class': 'form-control'}),
            'area_of_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Mention Industry/position you are in'}),
            'primary_skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Mention skills you have'}),
            'secondary_skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Mention secondary skills you have'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'in Years'}),
            'current_city': forms.TextInput(attrs={'class': 'form-control'}),
            'upload_resume': forms.FileInput(attrs={'class': 'form-control'}),
        }


class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ('name', 'contact', 'residence_address', 'business_address',
                  'profile_photo')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'residence_address': forms.Textarea(attrs={'class': 'form-control'}),
            'business_address': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'date', 'venue',
                  'description', 'thumbnail')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail':forms.FileInput(attrs={'class':'form-control'}),
        }

class EventPhotosForm(forms.ModelForm):

    class Meta:
        model = EventPhotos
        fields = ('event_photo',)

        widgets = {
            'event_photo':forms.FileInput(attrs={'class':'form-control','multiple':True})
        }


class MatrimonialForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=Matrimonial.GENDER_CHOICES, widget=forms.Select(attrs={ 'class': 'form-control'}))

    class Meta:
        model = Matrimonial
        fields = ('name', 'email', 'contact', 'gender',
                  'age', 'profile_photo', 'upload_bio_data')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'describe_youself': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control','placeholder':'Upload your profile photo'}),
            'upload_bio_data': forms.FileInput(attrs={'class': 'form-control','placeholder':'Upload your bio-data'}),
        }


class TrustMemberForm(forms.ModelForm):

    class Meta:
        model = TrustMember
        fields = ('name', 'occupation', 'contribution')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'contribution': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'image', 'url', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SponsorForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
