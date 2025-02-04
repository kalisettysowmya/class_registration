# registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('register/', views.register_student, name='register_student'),
    path('registered/<int:student_id>/', views.registered_courses, name='registered_courses'),
]
