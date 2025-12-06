from django.urls import path
from . import views

urlpatterns = [
    # Courses
    path('courses/', views.course_d, name='course'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
    path('courses/add', views.course_add, name='course_add'),
    # Trainers
    path('trainers/', views.trainer_d, name='trainer'),
    path('trainers/<int:id>/', views.trainer_detail, name='trainer_detail'),
    path('trainers/add', views.trainer_add, name='trainer_add'),
    # Students
    path('students/', views.student_d, name='student'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    path('students/add', views.student_add, name='student_add'),
    path('students/edit/<int:id>/', views.student_edit, name='student_edit'),
]
