from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.shortcuts import render

from books.forms import BookForm
from books.models import Book


# Create your views here.
class TopBooksView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/top_books.html'

    def get_queryset(self):
        return Book.objects.order_by("-title")[:5]


class CreateBookView(CreateView):
    model = Book
    template_name = 'book/create_book.html'
    form_class = BookForm

