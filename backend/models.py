from django.db import models

class Administration(models.Model):
    username = models.CharField(max_length=300)


class Parent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    job = models.CharField(max_length=200)

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    grades = models.FloatField()
    ranking = models.IntegerField()
    num_of_events_attended = models.IntegerField()
    absences = models.IntegerField()

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + self.last_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)


    student =models.ForeignKey(Student, on_delete=models.CASCADE)
