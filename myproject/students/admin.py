from django.contrib import admin
from .models import Student, Program, StudentProfile, CohortGroup

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['username', 'first_name', 'last_name', 'status']

@admin.register(StudentProfile)
class profileAdmin(admin.ModelAdmin):
  list_display = ['student','bio','date_of_birth','address','rating','profile_picture','date_join',]

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
  list_display = ['courses','grade','student']

@admin.register(CohortGroup)
class CohortAdmin(admin.ModelAdmin):
  list_display = ['name','date_join']

# admin.site.register(Student)
