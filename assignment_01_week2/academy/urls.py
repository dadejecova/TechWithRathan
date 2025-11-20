from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_d, name='course'),
    path('trainers/', views.trainer_d, name='trainer'),
    path('students/', views.student_d, name='student'),
]
