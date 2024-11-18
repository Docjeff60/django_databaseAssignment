from django.urls import path
from . import views
from .home import HomepageView

urlpatterns = [
    path('', views.cohort_home, name='studenthome' ),
    path('student/<slug:slug>/', views.student_detail, name='student_detail'),   
    # path('homeview/', HomepageView.as_view(), name='homeview'),
    path('studentabout/', views.about_cohort, name='studentabout'),
    path('send_message/<int:id>', views.send_message, name='send_message'), # New route


]