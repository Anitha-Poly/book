from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    print(book.title)
    # return HttpResponse("Book:" +book.title) 
    return render(request,"book_details.html",{'book':book})
