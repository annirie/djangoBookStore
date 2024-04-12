from django.urls import path, re_path

from .views import TopBookListView, CreateBookView, AllBookListView, BookDetailView

urlpatterns = [
    path('', AllBookListView.as_view(), name='all_book_list'),
    # path('<slug:title>/', BookDetailView.as_view(), name='book_detail'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('top_books/', TopBookListView.as_view(), name='top_book_list'),
    path('create_book/', CreateBookView.as_view(), name='create_book'),
]
