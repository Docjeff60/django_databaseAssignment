from django.contrib import admin
from .models import Student,Program,Student_Profile,CohortGroup

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name','status']




@admin.register(Student_Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student','date_of_birth', 'rating','date_join','address']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['student','grade','courses']



@admin.register(CohortGroup)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_count', 'date_join')  # Display cohort name, student count, and date joined

    def student_count(self, obj):
        return obj.students.count()  # Displays the total number of students in this cohort

    student_count.short_description = 'Number of Students'



# Register your models here.
# admin.site.register(Student)
# admin.site.register(Program)
# admin.site.register(Student_Profile)
# admin.site.register(CohortGroup)