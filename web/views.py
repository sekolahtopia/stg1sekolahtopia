from django.shortcuts import render
from .models import School

# Create your views here.

def home(request):
    schools = School.objects.all()
    return render(request, 'web/home.html', { 'schools' : schools })

def allschool(request):
    schools = School.objects.all()
    return render(request, 'web/allschool.html', { 'schools' : schools })
