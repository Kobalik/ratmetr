from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)