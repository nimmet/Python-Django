from django.shortcuts import render,HttpResponse,Http404,get_object_or_404
from django.db import models
from book_outlet.models import Book
from django.db.models import Avg, Max, Min

# Create your views here.

data =[
    [1,'Lord of the Rings',  3, "KJR", True],
    [2,'Uyghuristan history', 5, "Atilla", True],
    [3,'Java programming', 5, "Camilla", True],
    ]

def index(request):
    books  = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    
    return render(request,"book_outlet/index.html", {"books":books,
                                                     "total_number_of_books":num_books,
                                                     "average_rating":avg_rating})

def book_detail(request,slug):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
     })
    


def insert_data(request):
    for value in data:
        book = Book(value[0],value[1],value[2],value[3],value[4])
        book.save()
        # Book.objects.create(value[0],value[1],value[2],value[3],value[4])
    return HttpResponse('<h1>Book saved</h1>')