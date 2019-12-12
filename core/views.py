from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def homepage(request):
    return HttpResponse('hi')

def about (request):
    student =Student.objects.first()
     
    context={
        "name": student.name,
        "address": student.address
    }

    page = "about.html"
    return render(request,page,context)
    