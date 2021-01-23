from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, Books

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = Todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = Todo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    author = form["book_author"]
    price = form["book_price"]
    genre = form["book_genre"]
    description = form["book_description"]
    year = form["book_year"]
    b = Books(title=title, subtitle = subtitle, author=author, price=price, genre=genre, description=description, year=year)
    b.save()
    return redirect(books)

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)


def delete_book(request, id):
    b = Books.objects.get(id=id)
    b.delete()
    return redirect(books)

def mark_book(request, id):
    b = Books.objects.get(id=id)
    b.is_favorites = True
    b.save()
    return redirect(books)

def unmark_book(request, id):
    b = Books.objects.get(id=id)
    b.is_favorites = False
    b.save()
    return redirect(books)


def BooksDetail(request, id):
    book_object = Books.objects.get(id=id)
    return render(request, "book_detail.html", {"book_object": book_object})

def close_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)