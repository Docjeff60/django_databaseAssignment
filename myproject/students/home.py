from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Student, CohortGroup, Student_profile, Program
from django.core.paginator import Paginator


# Create your views here.

class HomepageView(View):
    def get(self, request):
        all_students = Student.objects.all()
        studentpagnation = Paginator(all_students, 2)
        page_numbers = request.GET.get('page')
        page_info = studentpagnation.get_page(page_numbers)
        pages = studentpagnation.page(2)


        context = {'student': page_info}
        return render(request, 'newstud/index.html', context= context)
    
 
# class StudentDetailView(View):
#     def get(self, request, pk):
#         try:
#             student_personal_info = Student.objects.get

#         except Student.DoesNotExist:
#             return redirect('404')
        
#         context = {
#             'student' :student_personal_info
#         }


#         return render(request, 'newstud/about.html', context)

