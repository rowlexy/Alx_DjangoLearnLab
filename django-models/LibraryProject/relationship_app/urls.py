from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register, user_login, user_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogOutView
urlpatterns = [
    path("views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]