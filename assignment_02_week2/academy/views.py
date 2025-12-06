from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from .models import course,student,trainer
from .forms import StudentForm, TrainerForm, CourseForm, EditStudentForm, EditTrainerForm, EditCourseForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

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

@login_required
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course')
        else:
            print(form.errors)
    form = CourseForm()
    context = {
        'form': form,
    }
    return render(request, 'academy/course/course_add.html', context)

@login_required
def course_edit(request, id):
    coursepk = get_object_or_404(course, id = id)
    if request.method == 'POST':
        form = EditCourseForm(request.POST, request.FILES, instance = coursepk)
        if form.is_valid():
            form.save()
            return redirect('course')
    form = EditCourseForm(instance = coursepk)
    context = {
        'form': form,
        'course': coursepk
    }
    return render(request, 'academy/course/course_edit.html', context)

@login_required
def course_delete(request, id):
    courses = get_object_or_404(course, id = id)
    courses.delete()
    return redirect('course')

@login_required

def trainer_add(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer')
        else:
            print(form.errors)
    form = TrainerForm()
    context = {
        'form': form,
    }
    return render(request, 'academy/trainer/trainer_add.html', context)


@login_required
def trainer_edit(request, id):
    trainerpk = get_object_or_404(trainer, id = id)
    if request.method == 'POST':
        form = EditTrainerForm(request.POST, request.FILES, instance = trainerpk)
        if form.is_valid():
            form.save()
            return redirect('student')
    form = EditTrainerForm(instance = trainerpk)
    context = {
        'form': form,
        'trainer': trainerpk
    }
    return render(request, 'academy/trainer/trainer_edit.html', context)


@login_required
def trainer_delete(request, id):
    trainers = get_object_or_404(trainer, id = id)
    trainers.delete()
    return redirect('trainer')


@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            print(form.errors)
    form = StudentForm()
    context = {
        'form': form,
    }
    return render(request, 'academy/student/student_add.html', context)


@login_required
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
        'student': studentpk
    }
    return render(request, 'academy/student/student_edit.html', context)


@login_required
def student_delete(request, id):
    students = get_object_or_404(student, id = id)
    students.delete()
    return redirect('student')