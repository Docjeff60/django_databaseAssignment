from django.urls import path
from . import views

urlpatterns = [
    path('', views.cohort_home, name='studenthome' ),
    path('studentabout/', views.about_cohort, name='studentabout')
    
]