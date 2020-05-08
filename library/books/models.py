from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(
        "Author", related_name="books"
    )
    ISBN = models.IntegerField()
    category = models.CharField(max_length=50)
    release_date = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()
