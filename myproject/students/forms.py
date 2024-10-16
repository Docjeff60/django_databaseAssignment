# students/forms.py
from django import forms
from .models import Student, Student_Profile

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'status']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student_Profile
        fields = ['bio', 'date_of_birth', 'address', 'rating', 'profile_picture']
