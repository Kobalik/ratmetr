from django.db import models
from students.models import Student
from subjects.models import Subject

class Mark(models.Model):
    mark = models.CharField(max_length=2)
    mark_type = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.mark
