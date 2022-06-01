from django.contrib import admin
from .models import Directory, Event, EventPhotos, JobSeeker, Matrimonial, TrustMember , Ad , EventPhotos

# Register your models here.
admin.site.register(Event)
admin.site.register(JobSeeker)
admin.site.register(Directory)
admin.site.register(Matrimonial)
admin.site.register(TrustMember)
admin.site.register(Ad)
admin.site.register(EventPhotos)