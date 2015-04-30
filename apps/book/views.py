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
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic import View




import requests
import json
from django.http import HttpResponse
from library.settings.base import SKILLTREE_API_URL, SKILLTREE_API_KEY
from library.core.utils import to_dict



from apps.book.models import BookLease, Book
from apps.libraryuser.models import Fellow
from apps.book.forms import AddForm, LendBookForm, BookEditForm
from django.views.generic.edit import FormView


# Create your views here.
        
class BookListView(ListView):
    model = Book
    # paginate_by = 25

    def get_context_data(self, **kwargs):
        book_id = self.request.session.get('book_id')
        context = super(BookListView, self).get_context_data(**kwargs)
        context['form'] = LendBookForm()
        if book_id:
            book = Book.objects.get(pk=book_id)
            context['book'] = book
        return context


class BookLeaseListView(ListView):

    model = BookLease
    def get_context_data(self, **kwargs):
        context = super(BookLeaseListView, self).get_context_data(**kwargs)
        # context['form'] = LendBookForm()
        return context


class BookDetailView(DetailView):

    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        return context


def get_book(request, id=None, template_name = 'book_new.html' ):
    user = request.user

    if id:
        book = get_object_or_404 (Book, pk=id)

    if request.POST:

        form = AddForm(request.POST)
    # check whether form is valid

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
            session = request.session['status'] = 'borrow'
            messages.success(request, 'Lent out Successfully to.')
            return HttpResponseRedirect('/home/')
    else:
        form.fields['book'].initial = book

    return render(request, 'borrow_book.html', locals(), context_instance=RequestContext(request))


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)   
    # if request.method=='POST':
    if book:
        book.delete()
    return HttpResponseRedirect('/home/')


def edit_book(request, id=None):
    book = Book.objects.get(id = id)
    book.pk = id

    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return render(request, "updated.html", locals())
    else:
        form = BookEditForm(instance=book)

    return render(request, 'book_edit.html', locals(), context_instance = RequestContext(request))

class SkillTree():
    """docstring for SkillTree"""
    def __init__(self):
        self.url = SKILLTREE_API_URL
        self.headers = {'X-AUTH-TOKEN': SKILLTREE_API_KEY}

    def fetch_data(self, url=None, **kwargs):
        ''' Method to fetch data fom skilltree
            :param url: The url to request data from, default is the instance url
            :param kwargs: Any other extra keyword parameters
        '''
        url = url or self.url
        get_results = []
        page = 1
        while True:
            params = {'page': page}
            response = requests.get(url, params=params, data=json.dumps(kwargs), headers=self.headers)
            if response.status_code == 404 or not response.json():
                break
            get_results.extend(response.json())
            page += 1        
        return get_results


def get_fellow_info():
    from apps.libraryuser.models import Fellow

    skill = SkillTree() 
    results = skill.fetch_data()
    print results
    num_results = len(results)
    print num_results
    for index in xrange(num_results):
        fellow = results[index]
        try:
            person = Fellow.objects.get(first_name=fellow.get('first_name'), last_name=fellow.get('last_name'))  
        except Exception, e:
            new_fellow = Fellow(first_name=fellow.get('first_name'), last_name=fellow.get('last_name'), email=fellow.get('email'))
            new_fellow.save()
            continue
    return 'done'



