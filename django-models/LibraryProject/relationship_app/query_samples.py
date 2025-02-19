from relationship_app.models import Author, Book, Library, Librarian

def books_by_specific_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"{author_name} not found"
    
def list_of_books(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"{library_name} not found"
def librarian_for_library(librarian_name):
    try:
        library = Librarian.objects.get(library=librarian_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return f"{librarian_name} not found"