from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login),
    path('logout/', views.logout),
    path('changePassword/', views.changePassword),
    path('forgotpass/', views.forgotpass),

    path('dashboard/', views.dashboard),
    path('appointment/', views.allclinic),
    url(r'^appointment/(\d+)/', views.paappointment),
    url(r'^info/(\w+)/appoint/(\d+)/', views.appointment),
    url(r'^info/(.+)/', views.diseaseInfo),
    url(r'^sendPincodeSMS/(\d+)/(\w+)/', views.sendPincodeSMS),
    url(r'^sendPincodeEmail/(\d+)/(\w+)/', views.sendPincodeEmail),
    path('sendSMStoAll/', views.sendSMStoAll),
    path('sendEmailtoAll/', views.sendEmailtoAll),

    path('clinic/', views.clinic),
    url(r'^clinic/edit/(\d+)', views.editClinic),
    url(r'^clinic/delete/(\d+)', views.deleteClinic),

    path('disease/', views.disease),
    url(r'^disease/edit/(\d+)', views.editDisease),
    url(r'^disease/delete/(\d+)', views.deleteDisease),

    path('adminManager/', views.adminManager),
    url(r'^adminManager/edit/(\d+)', views.editAdminManager),
    url(r'^adminManager/delete/(\d+)', views.deleteAdminManager),

    path('patients/', views.patients),
    url(r'^patients/edit/(\d+)', views.editPatients),
    url(r'^patients/delete/(\d+)', views.deletePatients),

    path('consultation/', views.consultation),
    url(r'^consultation/edit/(\d+)', views.editConsultation),
    url(r'^consultation/delete/(\d+)', views.deleteConsultation),
]