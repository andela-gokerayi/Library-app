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


def login (request):  
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('book-list'))
        else:
            return render_to_response('login_error.html')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

