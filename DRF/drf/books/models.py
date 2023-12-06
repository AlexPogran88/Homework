from django.db import models


class Books(models.Model):
    book_title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_genre = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
         return f"{self.book_title} | {self.author}  | {self.book_genre} | {self.price}"