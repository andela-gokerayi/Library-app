from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.book.models import BookLease, Book
from apps.libraryuser.models import Fellow
from apps.book.forms import AddForm, LendBookForm

# Create your views here.


class BookListView(ListView):

    model = BookLease

    def dispatch(self, *args, **kwargs):
        return super(BookListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context


class BookDetailView(DetailView):

    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        print context
        return context

# @login_required
# def get_book(request):
#     # if this is a POST request we need to process the form data
#     user = request.user
#     print user
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = AddForm(request.POST)
#         print form
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return render(request, "thank_you.html", locals())


#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AddForm()
#         # alert('Please fill all fields')

#     return render(request, 'book_new.html', {'form': form})



def get_book(request, id=None, template_name = 'book_new.html' ):
    user = request.user

    if id:
        book = get_object_or_404 (Book, pk=id)

    if request.POST:

        # book = get_object_or_404(Book, id=request.POST.get('id'))

        form = AddForm(request.POST)
    # check whether form is valid

        if form.is_valid():
            form.save()

        return render(request, "thank_you.html", locals())

    else:
        form = AddForm()

    return render_to_response (template_name, {'form': form,},context_instance = RequestContext(request))


#     context = {'book_form': book_form, 'book': book}
#     return render(request, 'borrow_book.html', context)

# def get(self, request):

#     book_form = AddForm()
#     context = {'book_form': book_form}
#     return render(request, 'book_new.html', context)


@login_required
def borrow_book(request):
    # if this is a POST request we need to process the form data
    user = request.user
    print user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LendBookForm(request.POST)
        form.fields['borrower'].queryset = Fellow.objects.all()

        print form
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return render_to_response("book_new.html", RequestContext(request))
            return HttpResponseRedirect('book-list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LendBookForm()
        # alert('Please fill all fields')

    return render(request, 'borrow_book.html', {'form': form})
