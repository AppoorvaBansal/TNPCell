
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('',views.Student_Home,name='Student_Home' ),
    path('notification/',views.notification,name='notification')
]
