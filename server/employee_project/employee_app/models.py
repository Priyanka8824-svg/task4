from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=20)
    emp_dept = models.CharField(max_length=20)
    emp_address = models.TextField()
    