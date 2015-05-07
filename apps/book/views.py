from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic import View
from django.views.generic.edit import FormView


from apps.book.models import BookLease, Book
from apps.libraryuser.models import Fellow
from apps.book.forms import AddForm, LendBookForm, BookEditForm

        
class BookListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        book_id = self.request.session.get('book_id')
        context = super(BookListView, self).get_context_data(**kwargs)
        context['form'] = LendBookForm()
        if book_id:
            book = Book.objects.get(pk=book_id)
            context['book'] = book
        return context

class BookDetailView(DetailView):

    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        return context


class BookLeaseListView(ListView):

    model = BookLease
    def get_context_data(self, **kwargs):
        context = super(BookLeaseListView, self).get_context_data(**kwargs)
        return context


class BookLeaseDetailView(DetailView):

    model = BookLease

    def get_context_data(self, **kwargs):
        context = super(BookLeaseDetailView, self).get_context_data(**kwargs)
        return context


def get_book(request, id=None, template_name = 'book_new.html'):
    user = request.user
    if id:
        book = get_object_or_404 (Book, pk=id)
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thank_you.html", locals())
    else:
        form = AddForm()
    return render(request, 'book_new.html', {'form': form,},context_instance = RequestContext(request))


@login_required
def borrow_book(request, id=None):
    user = request.user
    book = Book.objects.get(id=id)
    form = LendBookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            book_id = request.POST.get('book')
            book = Book.objects.get(pk=book_id)
            request.session['book_id'] = book_id
            form.save()
            # request.session['borrower'] = borrower
            messages.success(request, 'Lent out Successfully')
            return HttpResponseRedirect('/home/')
    else:
        form.fields['book'].initial = book

    return render(request, 'borrow_book.html', locals(), context_instance=RequestContext(request))


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)   
    if book:
        book.delete()
        session = request.session['status'] = 'delete'
        messages.warning(request, 'has been deleted')
    return HttpResponseRedirect('/home/')


def edit_book(request, id=None):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return render(request, "updated.html", locals())
    # else:
    #     # form = BookEditForm(instance=book)
    #     form.fields['book'].initial=book
    return render(request, 'book_edit.html', locals(), context_instance = RequestContext(request))
