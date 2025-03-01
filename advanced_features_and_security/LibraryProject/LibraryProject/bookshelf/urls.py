from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register, user_login, user_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogOutView
from .views import admin_view
from .views import librarian_view
from .views import member_view
urlpatterns = [
    path("views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('admin/dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('member/dashboard/', member_view.member_dashboard, name='member_dashboard'),
    path('librarian/dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
]
