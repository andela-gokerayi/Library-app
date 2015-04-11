from django.shortcuts import render, render_to_response
from book.models import Book, BookStatus
from django.views.generic.list import ListView
from .forms import AddForm
# from library.services.decorators import staff_or_403
# from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    # return HttpResponse("Hopefully it works oo!")
    return render_to_response('index.html')

class BookListView(ListView):

    model = BookStatus

    # @method_decorator(staff_or_403)
    def dispatch(self, *args, **kwargs):
        return super(BookListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context


def get_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('home/books/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddForm()

    return render(request, 'book_new.html', {'form': form})