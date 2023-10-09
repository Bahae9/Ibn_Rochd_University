from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


    student_related_name = 'student_user'
    parent_related_name = 'parent_user'
    module_related_name = 'module_user'
    teacher_related_name = 'teacher_user'

    # Change related_name for groups and user_permissions
    groups = models.ManyToManyField('auth.Group', related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='user_permissions', blank=True)

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name=User.teacher_related_name)

    def __str__(self) -> str:
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    teachers = models.ManyToManyField(Teacher, related_name='students', blank=True, null=True)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name=User.student_related_name)

    def __str__(self) -> str:
        return self.full_name

class Parent(models.Model):
    full_name = models.CharField(max_length=200)
    child = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents', blank=True, null=True)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name=User.parent_related_name)

    def __str__(self) -> str:
        return self.full_name

class modules(models.Model):
    name = models.CharField(max_length=200)
    cof = models.SmallIntegerField()

    students = models.ManyToManyField(Student, related_name='modules_for_students', blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, related_name='modules_for_teachers', blank=True, null=True)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name=User.module_related_name)

    def __str__(self) -> str:
        return self.name
