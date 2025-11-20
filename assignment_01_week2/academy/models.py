from django.db import models
import datetime

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=50, verbose_name="Courses")
    description = models.CharField(max_length=200)
    duration = models.IntegerField() 
    course_image = models.ImageField(upload_to='course/')

    def __str__(self):
        return f"{self.course_name}"


class trainer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=50)
    salary = models.FloatField()
    trainer_photo = models.ImageField(upload_to='trainer/')
    joinin_date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.expertise}"

class student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(course, on_delete=models.SET_NULL, blank = True, null=True)
    trainer = models.ForeignKey(trainer, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"