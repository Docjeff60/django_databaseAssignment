from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import stud_exam_dashboard, student_dashboard

urlpatterns = [
    path('', stud_exam_dashboard, name='stud_exam_dashboard'),
    path('student_dashboard/<int:student_id>/', student_dashboard, name='student_dashboard'),
]

# serves as media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
