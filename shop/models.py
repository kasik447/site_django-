from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField() 
    reviews = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title