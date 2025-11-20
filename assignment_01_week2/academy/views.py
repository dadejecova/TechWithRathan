from django.shortcuts import render
from django.views.generic import ListView
from .models import course,student,trainer

# Create your views here.
def course_d(request):
    courses = course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'academy/course.html', context)

def trainer_d(request):
    trainers = trainer.objects.all()
    context = {
        'trainers': trainers
    }
    return render(request, 'academy/trainer.html', context)

def student_d(request):
    students = student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'academy/student.html', context)