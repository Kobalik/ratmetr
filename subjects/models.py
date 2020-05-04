from django.db import models
from groups.models import Group

class Subject(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    subject_name = models.CharField(max_length=200)