from django.urls import path
from . import views


urlpatterns = [
    path('', views.land, name='land'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('students', views.Student_page, name='students'),
    path('teachers', views.Teacher_page, name='teachers'),
    path('administration_page', views.Administration_page,
         name='administration_page'),
    path('parents', views.Parent_page, name='parents'),
    path('index', views.index, name='index'),
    path('course-single', views.course_single, name='course-single'),
    path('parents-dashboard', views.parents_dashboard, name='parents-dashboard'),
    path('students-progress', views.students_progress, name='students-progress'),
    path('student-resources', views.student_resources, name='student-resources'),
    path('teachers-dashboard', views.teachers_dashboard, name='teachers-dashboard'),
    path('td-cours-publish', views.td_cours_publish, name='td-cours-publish'),
    path('grade-assignement', views.grade_assignement, name='grade-assignement'),
    path('logout', views.logout, name='logout')
]
