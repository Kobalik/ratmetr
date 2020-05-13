from django.db import models
from groups.models import Group

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    def __str__(self):
        return self.subject_name