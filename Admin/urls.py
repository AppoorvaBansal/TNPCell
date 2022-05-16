
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Admin import views

urlpatterns = [
    path('',views.admin_Dashboard,name='admin_Dashboard' ),
    path('Add_company/',views.add_Comapny,name='add_Company'),
    path('Add_Student/',views.add_Student,name='add_Student')
]
