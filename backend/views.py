from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Student, Teacher, Parent


def index(request):
    return render(request, 'frontend/index.html')

def land(request):
    return render(request, 'frontend/land-page.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        registration_type = str(request.POST['registration_type']).lower()
        registration_types = {
            'student' : Student,
            'teacher' : Teacher,
            'parent' : Parent,

        }
        if registration_type in registration_types.keys():
            if password == password2:
                if registration_types[registration_type].objects.filter(full_name=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('pages-register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('signup')
                else:
                    

                    user = get_user_model().objects.create_user(username=email, password=password)
                    
                    # Create a profile (student, teacher, parent, etc.) and associate it with the user
                    profile = registration_types[registration_type].objects.create(
                        full_name=username,
                        user=user
                    )
                    profile.save()
                    # Log the user in
                    auth.login(request, user)
                    
                    
                    # user_login = auth.authenticate(username=username, password=password)
                    # auth.login(request, user_login)

                    # # user_model = registration_types[registration_type].objects.get(username=username)
                    # # new_profile = Profile.objects.create(user= user_model, id_user=user_model.id)
                    # # new_profile.save()
                    return redirect('/')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('pages-register')
        else:
            messages.info(request, 'Please choose a valid registration type')
            return redirect('/')
    else:
        return render(request, 'frontend/pages-register.html', {})


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong password or Username')
            return redirect('signin')
    else:
        return render(request, 'frontend/pages-login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def Student_page(request):
    return render(request, 'frontend/student-section.html')

def Teacher_page(request):
    return render(request, 'frontend/teachers-section.html')

def Administration_page(request):
    return render(request, 'frontend/administration_page.html')

def Parent_page(request):
    return render(request, 'frontend/parents-section.html')


def index(request):
    return render(request, 'frontend/index.html')

def course_single(request):
    return render(request, 'frontend/course-single.html')

def parents_dashboard(request):
    return render(request, 'frontend/parent-dashboard.html')

def students_progress(request):
    return render(request, 'frontend/student-dashboard.html')

def student_resources(request):
    return render(request, 'frontend/student-resources.html')

def teachers_dashboard(request):
    return render(request, 'frontend/teacher-dashboard.html')

def td_cours_publish(request):
    return render(request, 'frontend/td-cours-publish.html')

def grade_assignement(request):
    return render(request, 'frontend/grade-assignement.html')