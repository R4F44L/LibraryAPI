from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author", related_name="books")
    ISBN = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    release_date = models.DateField()
    is_rented = models.BooleanField(default=False, null=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    rented_by = models.ForeignKey(
        User, related_name="rented_books", null=True, on_delete=models.DO_NOTHING
    )


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()
