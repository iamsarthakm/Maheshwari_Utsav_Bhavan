from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render
from mubApp.models import TrustMember
from mubApp.models import Directory
from mubApp.models import Matrimonial
from mubApp.models import Event
from mubApp.models import JobSeeker, EventPhotos
from mubApp.forms import AdminForm, JobSeekerForm, EventForm, MatrimonialForm, DirectoryForm, TrustMemberForm, AdForm, EventPhotosForm
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'mubApp/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def events(request):
    events = Event.objects.all()
    return render(request, 'mubApp/events.html', {'events': events})

def trustMembers(request):
    members = TrustMember.objects.all()
    return render(request, 'mubApp/trustMembers.html', {'members': members})

def jobs(request):

    if request.method == 'POST':

        job_seeker_form = JobSeekerForm(data=request.POST, files=request.FILES)

        if job_seeker_form.is_valid():
            JobSeeker = job_seeker_form.save()
            JobSeeker.save()
            submitted = True
            return render(request, 'mubApp/jobs.html', {'submitted': submitted})
    else:
        job_seeker_form = JobSeekerForm()
    return render(request, 'mubApp/jobs.html', {'job_form': job_seeker_form})

def matrimonial(request):
    if request.method == 'POST':

        matrimonial_form = MatrimonialForm(
            data=request.POST, files=request.FILES)

        if matrimonial_form.is_valid():
            Matrimonial = matrimonial_form.save()
            Matrimonial.save()
            submitted = True
            return render(request, 'mubApp/matrimonial.html', {'submitted': submitted})

        else:
            print(matrimonial_form.errors)
    else:
        matrimonial_form = MatrimonialForm()
    return render(request, 'mubApp/matrimonial.html', {'matrimonial_form': matrimonial_form})

def adminTrustMembers(request):

    if request.method == 'POST':

        trust_member_form = TrustMemberForm(data=request.POST)
        if trust_member_form.is_valid():
            trust_member = trust_member_form.save()
            print('found it')
            trust_member.save()
            submitted = True
            return render(request, 'mubApp/admin/trustMembers.html', {'submitted': submitted})

        else:
            print(trust_member_form.errors)
    else:
        trust_member_form = TrustMemberForm()
    return render(request, 'mubApp/admin/trustMembers.html', {'trust_member_form': trust_member_form})

def directory(request):
    if request.method == 'POST':

        directory_form = DirectoryForm(data=request.POST, files=request.FILES)
        if directory_form.is_valid():
            Directory = directory_form.save()
            print('found it')
            Directory.save()
            submitted = True
            return render(request, 'mubApp/directory.html', {'submitted': submitted})

        else:
            print(directory_form.errors)
    else:
        directory_form = DirectoryForm()
    return render(request, 'mubApp/directory.html', {'directory_form': directory_form})

def about(request):
    return render(request, 'mubApp/about.html')

def register(request):
    
    registered = False
    if request.method == 'POST':

        user_form = AdminForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = AdminForm()

    return render(request, 'mubApp/registration.html',
                  {'user_form': user_form,
                           'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('mubApp:adminJobs'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'mubApp/login.html', {})


def peopleDirectory(request):
    directorys = Directory.objects.all()
    return render(request, 'mubApp/peopleDirectory.html', {'directorys': directorys})


def adminPanel(request):
    return render(request, 'mubApp/admin/index.html')


def adminEvents(request):

    if request.method == 'POST':

        event_form = EventForm(data=request.POST, files=request.FILES)
        event_photos_form = EventPhotosForm(
            data=request.POST, files=request.FILES)
        if event_form.is_valid() and event_photos_form.is_valid():
            Event = event_form.save()
            event_photos = request.FILES.getlist('event_photo')

            for event_photo in event_photos:

                new_event_photo = EventPhotos.objects.create(
                    event=Event,
                    event_photo=event_photo
                )
                new_event_photo.save()

            Event.save()
            return render(request, 'mubApp/admin/events.html')

        else:
            print(event_form.errors)
    else:
        event_form = EventForm()
        event_photos_form = EventPhotosForm()
    return render(request, 'mubApp/admin/events.html', {'event_form': event_form, 'event_photos_form': event_photos_form})


def adminMatrimonial(request):
    matrimonials = Matrimonial.objects.all()

    return render(request, 'mubApp/admin/matrimonial.html', {'matrimonials': matrimonials})


def adminDirectory(request):
    directorys = Directory.objects.all()
    return render(request, 'mubApp/admin/directory.html', {'directorys': directorys})


def adminJobs(request):
    jobs = JobSeeker.objects.all()
    return render(request, 'mubApp/admin/jobs.html', {'jobs': jobs})


def sponsors(request):
    return render(request, 'mubApp/admin/sponsors.html')


def ads(request):

    if request.method == 'POST':

        ad_form = AdForm(data=request.POST, files=request.FILES)
        if ad_form.is_valid():
            ad = ad_form.save()
            print('found it')
            ad.save()
            return render(request, 'mubApp/admin/ads.html')

        else:
            print(ad_form.errors)
    else:
        ad_form = AdForm()
    return render(request, 'mubApp/admin/ads.html', {'ad_form': ad_form})


def showJobSeeker(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        job = JobSeeker.objects.get(pk=data['pk'])
    return render(request, 'mubApp/show/showJobSeekers.html', {'job': job})


def showEvent(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        event = Event.objects.get(pk=data['pk'])
        event_photos = EventPhotos.objects.filter(event=data['pk'])

    return render(request, 'mubApp/show/showEvents.html', {'event': event, 'event_photos': event_photos})

def showDirectory(request):
    if request.method == 'POST':
        data = request.POST
        directory = Directory.objects.get(pk=data['pk'])

    return render(request, 'mubApp/show/showDirectory.html', {'directory': directory})

@login_required
def showMatrimonial(request):
    if request.method == 'POST':
        data = request.POST
        matrimonial = Matrimonial.objects.get(pk=data['pk'])

    return render(request, 'mubApp/show/showMatrimonial.html', {'matrimonial': matrimonial})


class SearchView(ListView):
    model = Directory
    template_name = 'mubApp/peopleDirectory.html'
    context_object_name = 'directorys'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Directory.objects.filter(
                Q(name=query) | Q( contact=query)
            )
            result = postresult
        else:
            result = None
        return result

@login_required
def deleteJobSeeker(request):

    if request.method == 'POST':
        data = request.POST
        # print(data['email'])
        deleteSeeker = JobSeeker.objects.get(email=data['email'])
        deleteSeeker.delete()

    return HttpResponseRedirect(reverse('mubApp:adminJobs'))

@login_required
def deleteMatrimonial(request):

    if request.method == 'POST':
        data = request.POST
        # print(data)
        deleteMat = Matrimonial.objects.get(pk=data['pk'])
        deleteMat.delete()

    return HttpResponseRedirect(reverse('mubApp:adminMatrimonial'))

@login_required
def deleteDirectory(request):

    if request.method == 'POST':
        data = request.POST
        print(data)
        deleteDir = Directory.objects.get(pk=data['pk'])
        deleteDir.delete()

    return HttpResponseRedirect(reverse('mubApp:adminDirectory'))


@login_required
def deleteEvent(request):

    if request.method == 'POST':
        data = request.POST
        print(data)
        event = Event.objects.get(pk=data['pk'])
        event.delete()

    return HttpResponseRedirect(reverse('mubApp:adminEvents'))

@login_required
def deleteTrustMember(request):

    if request.method == 'POST':
        data = request.POST
        member = TrustMember.objects.get(pk=data['pk'])
        member.delete()

    return HttpResponseRedirect(reverse('trustMembers'))
