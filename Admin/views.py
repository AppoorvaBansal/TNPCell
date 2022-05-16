from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def admin_Dashboard(request):
    return HttpResponse("Welcome to ADmin dashboard")

def add_Comapny(request):
    return HttpResponse("HELLOOO")

def add_Student(request):
    return HttpResponse("HELLOO Students")

