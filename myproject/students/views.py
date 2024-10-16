from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Student_Profile
from .forms import StudentForm, StudentProfileForm


# View for student exam dashboard (including form handling)
def stud_exam_dashboard(request):
    # Handle form submissions
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)
        if student_form.is_valid() and profile_form.is_valid():
            student = student_form.save()
            profile = profile_form.save(commit=False)
            profile.student = student
            profile.save()
            return redirect('stud_exam_dashboard')  # Ensure the URL name is correct
    else:
        student_form = StudentForm()
        profile_form = StudentProfileForm()

    # Retrieve any students or additional context for displaying in the template
    students = Student.objects.all()  # Fetch all students to display in the table

    return render(request, 'stud_exam_dashboard.html', {
        'student_form': student_form,
        'profile_form': profile_form,
        'students': students,  # Pass students to the template for display
    })


# View for student profile
def student_dashboard(request, student_id):
    student = get_object_or_404(Student, id=student_id)  # Retrieve the student based on the ID
    return render(request, 'student_dashboard.html', {'student': student})
