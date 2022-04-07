from statistics import mode
from django.db import models


class Employee(models.Model):
 eno = models.IntegerField()
 ename = models.CharField(max_length=64)
 eadd = models.CharField(max_length=64)
 esalary = models.FloatField()

