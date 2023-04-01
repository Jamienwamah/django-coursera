from django.db import models

# Create your models here.

class employee(models.Model):
    employee_name = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    salary = models.CharField(max_length=200, default=None)

class menu(models.Model):
    item_menu = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(employee, on_delete=models.PROTECT, default=None, related_name="employee")

