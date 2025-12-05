from django import forms
from .models import student, course, trainer

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'


class TrainerForm(forms.ModelForm):
    class Meta:
        model = trainer
        fields = '__all__'