import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          serialize=False, editable=False, primary_key=True)

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.book.id})
