from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import random
import string




def email_validator(value):
   if '@' and '.com' in value:
      return value
   else:
      raise ValidationError('Invalid email address')


# Create your models here.

student_type = [
    ('leader', 'cohort leader'),
    ('deputy', 'vice leader'),
    ('Secretary', 'Secretary'),
    ('President', 'President'),
    ('member', 'member'),
]

class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    student_type = models.CharField(max_length=100, choices=student_type, default='member')
    email = models.EmailField(max_length=245, unique=True, validators=[email_validator])
    date_join = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_join']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self,*args, **kwargs ):
      if not self.slug:
          student_slug_num_gen  = "".join(random.choices(string.digits,k=9))
          self.slug = slugify(f"{self.first_name,self.last_name}-{student_slug_num_gen}")
      super().save(*args, **kwargs)




class Student_profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300)
    rating = models.FloatField(default=0.0)
    profile_picture = models.ImageField(upload_to='student_profile/')



    def __str__(self):
        return f"{self.student.username}"


class Program(models.Model):
    courses = models.CharField(max_length=500)
    grade = models.IntegerField(default=0.0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def str(self):
        return f"{self.courses}"


class CohortGroup(models.Model):
    name = models.CharField(max_length=200)
    date_join = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student, related_name= 'cohort')
    def str(self):
        return f"{self.name}"