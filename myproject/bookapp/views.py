from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# READ
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookapp/book_list.html', {'books': books})

# CREATE
def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
        )
        return redirect('book_list')
    return render(request, 'bookapp/add_book.html')

# UPDATE (price only)
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.price = request.POST['price']
        book.save()
        return redirect('book_list')
    return render(request, 'bookapp/update_book.html', {'book': book})

# DELETE
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# READ
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookapp/book_list.html', {'books': books})

# CREATE
def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
        )
        return redirect('book_list')
    return render(request, 'bookapp/add_book.html')

# UPDATE (price only)
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.price = request.POST['price']
        book.save()
        return redirect('book_list')
    return render(request, 'bookapp/update_book.html', {'book': book})

# DELETE
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookapp/delete_book.html', {'book': book})