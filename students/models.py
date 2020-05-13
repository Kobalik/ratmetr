from django.db import models
from groups.models import Group

class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    is_budget = models.BooleanField(default=False)
    def __str__(self):
        return self.surname