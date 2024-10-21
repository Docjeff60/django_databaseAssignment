from django.shortcuts import render
from .models import Student


# Create your views here.

def cohort_home(request):
    students = Student.objects.all()
    return render(request, "index.html", {
        'students': students
    })


def about_cohort(request): 
    return render(request, "about.html")