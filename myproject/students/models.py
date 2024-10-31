from django.db import models

# Create your models here.


student_type = [
  ('leader', 'cohort leader'),
  ('deputy', 'vice leader'),
  ('Secretary', 'Secretary'),
  ('President', 'President'),
  ('member', 'member'),
]

class Student(models.Model):
  username = models.CharField(max_length=100)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  status = models.BooleanField(default=True)
  student_type = models.CharField(max_length=100, choices=student_type, default='member')

  def str(self):
    return f"{self.first_name} {self.last_name}"


class Student_profile(models.Model):
  student = models.OneToOneField(Student, on_delete=models.CASCADE)
  bio = models.TextField()
  date_of_birth = models.DateField()
  address = models.CharField(max_length=300)
  rating = models.FloatField(default=0.0)
  profile_picture = models.ImageField(upload_to= 'student_profile')
  date_join = models.DateTimeField(auto_now_add=True)

  def str(self):
    return f"{self.student.username}"


class Program(models.Model):
  courses = models.CharField(max_length=500)
  grade = models.IntegerField(default=0.0)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  def str(self):
    return f"{self.courses} "


class CohortGroup(models.Model):
  name = models.CharField(max_length=200)
  date_join = models.DateTimeField(auto_now_add=True)
  students = models.ManyToManyField(Student)
  def str(self):
    return f"{self.name}"