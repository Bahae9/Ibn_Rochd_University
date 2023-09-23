from django.urls import path
from . import views


urlpatterns = [
    path('', views.land, name='land'),
    path('land', views.land, name='land'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('students', views.Student_page, name='students'),
    path('teachers', views.Teacher_page, name='teachers'),
    path('administration_page', views.Administration_page, name='administration_page'),
    path('parents', views.Parent_page, name='parents'),
]
