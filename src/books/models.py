from app.models import TimestampedModel
from django.db import models
from django.db.models.manager import Manager


class Author(TimestampedModel):
    name = models.CharField(max_length=255)
    books: "Manager[Book]"


class Book(TimestampedModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    name = models.CharField(max_length=255)
