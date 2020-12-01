from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):
    author = models.CharField(max_length=100)
