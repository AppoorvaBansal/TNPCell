from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Student_Home(request):
    return HttpResponse("Welcome to Student dashboard")

def show_Comapny(request):
    return HttpResponse("COMPANY DETAILS")

def notification(request):
    return HttpResponse("Notification")
