from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()


class Branch(models.Model):
    city = models.CharField(max_length=100)
    origin = models.DateField()
    contact = models.EmailField()
    employees = models.IntegerField()

    class Meta:
        verbose_name_plural = "Branches"


class People(models.Model):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "People"
