from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic.list import ListView
from apps.book.models import Book
from django.core.context_processors import csrf



class HomeView(View):

    def get(self, request):
        return render_to_response('index.html', locals())


class BookIndexListView(ListView):

    model = Book

    def dispatch(self, *args, **kwargs):
        return super(BookIndexListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookIndexListView, self).get_context_data(**kwargs)
        return context

# Class Based Login View
class LoginView(View):

    def get(self, request):
        return render_to_response('login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)
            print user
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('books-list'), locals())
            else:
                print HttpResponseRedirect(reverse('book-index'))

        return HttpResponseRedirect(reverse('book-index'))

# Class Based Logout View
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('book-index'), locals())


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thank_you.html", locals())

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('signup.html', args)

