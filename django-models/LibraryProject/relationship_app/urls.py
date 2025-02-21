from django.urls import path
from .views import LibraryDetailView
from .views import list_of_books
urlpatterns = [
    path('books/', list_of_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]