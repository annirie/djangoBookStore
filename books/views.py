from django.views.generic import ListView, CreateView, DetailView

from django.shortcuts import render

from books.forms import BookForm
from books.models import Book


# Create your views here.
class TopBookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/top_books.html'

    def get_queryset(self):
        return Book.objects.order_by("-title")[:5]


class CreateBookView(CreateView):
    model = Book
    template_name = 'book/create_book.html'
    form_class = BookForm


class AllBookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/all_book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'
