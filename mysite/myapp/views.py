from django.core.exceptions import RequestAborted
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Import your models here.
from .models import Book
from .forms import BookForm


# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list' : book_list
    }
    return render(request, 'myapp/index.html', context)

def detail(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html', {'book':book}) 

def add_book(request):
    # form submission
    if request.method == 'POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']

        book = Book(name=name, desc=desc, price=price, book_image=book_image)
        book.save()
        return redirect('/')
    return render(request, 'myapp/add_book.html')

# NOTE: as i understand it, the flow is that the id of the book is passed as an integer into the url first, then the url takes that value and passes it into the view (which is why the view accepts the id as an argument)
def update(request,book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html',{'book':book, 'form':form})

def delete(request,book_id):
    
    if request.method=='POST':
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')