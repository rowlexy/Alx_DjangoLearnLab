from django.shortcuts import render
from django.http import HttpResponse
from . models import Book, Library
from django.views.generic import DetailView
# Create your views here.
def list_of_books(request):
    books = Book.objects.all()
    book_list = [f"{book.title} {book.author.name}" for book in books]
    context = "\n".join(book_list)
    return HttpResponse(context, content_type="text/plain")

class LibraryDetailView(DetailView):
   model = Library 
   template_name = "relationship_app/library_detail.html"
   context_name = "library"

   def context_data(self, **kwargs):
       context = super().context_data(**kwargs)
       context["books"] = self.object.books.all()
       return context
