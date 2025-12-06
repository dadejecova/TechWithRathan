from django import forms
from .models import student, course, trainer

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
        widgets = {
            'joining_date': forms.DateInput(attrs={'type':'date'})
        }


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = {
            'first_name',
            'last_name',
            'email',
            'is_active',
            'enrolled_course',
            'trainer',
            'student_image',
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'
        widgets = {
            'joining_date': forms.DateInput(attrs={'type':'date'})
        }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = trainer
        fields = '__all__'
        widgets = {
            'joining_date': forms.DateInput(attrs={'type':'date'})
        }