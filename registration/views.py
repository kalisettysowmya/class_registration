# registration/views.py
from django.shortcuts import render, redirect
from .models import Course, Student

def course_list(request):
    # Display all available courses
    courses = Course.objects.all()
    return render(request, 'registration/course_list.html', {'courses': courses})

def register_student(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        course_ids = request.POST.getlist('courses')  # Get selected course IDs

        # Create or update student
        student, created = Student.objects.get_or_create(email=email, defaults={'name': name})
        if not created:
            student.name = name
            student.save()

        # Add selected courses to the student
        student.courses.set(course_ids)

        return redirect('registered_courses', student_id=student.id)

    # If GET request, show the registration form
    courses = Course.objects.all()
    return render(request, 'registration/register_student.html', {'courses': courses})

def registered_courses(request, student_id):
    # Display courses registered by a student
    student = Student.objects.get(id=student_id)
    courses = student.courses.all()
    return render(request, 'registration/registered_courses.html', {'student': student, 'courses': courses})
