from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from .models import course,student,trainer
from .forms import StudentForm, TrainerForm, CourseForm, EditStudentForm
from django.contrib.auth.models import User

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


def student_detail(request,id):
    students = get_object_or_404(student, id=id)
    context = {
        'students': students
    }
    print(context)
    return render(request, 'academy/student/student_detail.html', context)


def trainer_detail(request,id):
    trainers = get_object_or_404(trainer, id=id)
    context = {
        'trainers': trainers
    }
    print(context)
    return render(request, 'academy/trainer/trainer_detail.html', context)


def course_detail(request,id):
    courses = get_object_or_404(course, id=id)
    context = {
        'courses': courses
    }
    print(context)
    return render(request, 'academy/course/course_detail.html', context)


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = CourseForm()
    context = {
        'form': form,
    }
    return render(request, 'academy/course/course_add.html', context)


def trainer_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = CourseForm()
    context = {
        'form': form,
    }
    return render(request, 'academy/trainer/trainer_add.html', context)


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = StudentForm()
    context = {
        'form': form,
    }
    return render(request, 'academy/student/student_add.html', context)


def student_edit(request, id):
    studentpk = get_object_or_404(student, id = id)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, request.FILES, instance = studentpk)
        if form.is_valid():
            form.save()
            return redirect('student')
    form = EditStudentForm(instance = studentpk)
    context = {
        'form': form,
    }
    return render(request, 'academy/student/student_detail.html', context)