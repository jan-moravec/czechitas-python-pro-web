from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    city = models.CharField(max_length=100)
    origin = models.DateField()
    contact = models.EmailField()
    employees = models.IntegerField()

    def courses(self):
        return Course.objects.filter(branch=self)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.city


class People(models.Model):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self.first_name + ' ' + self.family_name
