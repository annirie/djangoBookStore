import uuid

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
