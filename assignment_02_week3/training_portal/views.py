from django.http import HttpResponse
from academy.models import course, student, trainer
from django.shortcuts import render

def home(request):
    students_total = student.objects.all().count()
    trainers_total = trainer.objects.all().count()
    courses_total = course.objects.all().count()
    context = {
        'courses_total': courses_total,
        'trainers_total': trainers_total,
        'students_total': students_total,
    }
    return render(request, 'home.html', context)

