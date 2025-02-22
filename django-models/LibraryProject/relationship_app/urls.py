from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register, user_login, user_logout
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]