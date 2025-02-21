from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic import DetailView
# Create your views here.
def list_of_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }

    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
   model = Library 
   template_name = "relationship_app/library_detail.html"
   context_name = "library"

   def context_data(self, **kwargs):
       context = super().context_data(**kwargs)
       context["books"] = self.object.books.all()
       return context
