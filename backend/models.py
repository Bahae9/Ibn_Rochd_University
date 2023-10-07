from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Administration(models.Model):
    username = models.CharField(max_length=300)


class Parent(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    job = models.CharField(max_length=200)


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    grades = models.FloatField(blank=True)
    ranking = models.IntegerField(blank=True)
    num_of_events_attended = models.IntegerField(blank=True)
    absences = models.IntegerField(blank=True)

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, blank=True)

    def create_student(email, password, first_name, last_name=None, grades=None, ranking=None, num_of_events_attended=None, absences=None):
        user = User.objects.create_user(
            username=first_name, email=email, password=password)
        student = Student.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            grades=grades,
            ranking=ranking,
            num_of_events_attended=num_of_events_attended,
            absences=absences
        )

    def __str__(self):
        return self.first_name + self.last_name


class Teacher(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Ntesti(models.Model):
    name = models.CharField(max_length=200)
    grades = models.FloatField()
    # email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
