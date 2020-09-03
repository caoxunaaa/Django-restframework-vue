from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name
