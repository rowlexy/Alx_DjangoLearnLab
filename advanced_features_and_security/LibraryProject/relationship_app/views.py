from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.succcess(request, 'Registrationsuccessful!')
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def user_login(request):
    request.method == 'POST'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("book-list")
    else:
            messages.error(request, "Invalid username or password.")

    return render(request, "relationship_app/login.html")

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
   model = Library 
   template_name = "relationship_app/library_detail.html"
   context_name = "library"

   def context_data(self, **kwargs):
       context = super().context_data(**kwargs)
       context["books"] = self.object.books.all()
       return context


