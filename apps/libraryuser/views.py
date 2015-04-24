from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic.list import ListView
from django.core.context_processors import csrf
from apps.book.models import Book
from library.services import skilltreeapi



class HomeView(View):

    def get(self, request):
        return render_to_response('base.html', locals())


class BookIndexListView(ListView):

    model = Book

    def dispatch(self, *args, **kwargs):
        return super(BookIndexListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookIndexListView, self).get_context_data(**kwargs)
        return context


def login (request):
    print request
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    print request
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    print user

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('book-index'))

    else:
        return HttpResponseRedirect(reverse('login'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

