from django.urls import path

from .views import TopBooksView, CreateBookView

urlpatterns = [
    path('top_books/', TopBooksView.as_view(), name='top_books'),
    path('create_book/', CreateBookView.as_view(), name='create_book')
]
