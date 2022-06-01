from django.urls import path
from . import views


app_name= 'mubApp'

urlpatterns = [
    path('adminPanel/',views.adminPanel,name='adminPanel'),
    path('events/',views.adminEvents,name='adminEvents'),
    path('showEvent/',views.showEvent,name='showEvent'),
    path('deleteEvent/',views.deleteEvent,name='deleteEvent'),
    path('matrimonial/',views.adminMatrimonial,name='adminMatrimonial'),
    path('showMatrimonial/',views.showMatrimonial,name='showMatrimonial'),
    path('deleteMatrimonial/',views.deleteMatrimonial,name='deleteMatrimonial'),
    path('directory/',views.adminDirectory,name='adminDirectory'),
    path('showDirectory/',views.showDirectory,name='showDirectory'),
    path('deleteDirectory/',views.deleteDirectory,name='deleteDirectory'),
    path('jobs/',views.adminJobs,name='adminJobs'),
    path('showJobSeeker/',views.showJobSeeker,name='showJobSeeker'),
    path('deleteJobSeeker/',views.deleteJobSeeker,name='deleteJobSeeker'),
    path('trustMembers/',views.adminTrustMembers,name='adminTrustMembers'),
    path('deleteTrustMember/',views.deleteTrustMember,name='deleteTrustMember'),
    path('sponsors/',views.sponsors,name='sponsors'),
    path('ads/',views.ads,name='ads'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
