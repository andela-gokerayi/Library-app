""" This file is supposed to run in the background.
    For now it will return an http response."""

from __future__ import absolute_import

from celery import shared_task
from apps.book.models import BookLease
from apps.libraryuser.models import Fellow
from django.core.mail import send_mail
from django.utils import timezone
from django.db.models import Q
from django.core.mail import send_mail
import datetime
from django.http import HttpResponse, HttpResponseRedirect

#@shared_task
def send_admin_mail(*args, **kwargs):
    afteroneday = datetime.date.today() + datetime.timedelta(days=1)
    aftertwodays = datetime.date.today() + datetime.timedelta(days=2)
    due_date = datetime.date.today()
    borrowed_books = BookLease.objects.filter(Q(due_date=aftertwodays) | 
        Q(due_date=afteroneday) |  Q(due_date__lte=due_date)).values_list('borrower__email', 'book__title', 'book__id')

    list_borr = {e[0]:[] for e in borrowed_books}

    for e in borrowed_books:
        list_borr[e[0]].append(e[1])

    for names, books in list_borr.items():
        name = names.split('.')[0] or names
        book = ' and '.join(books)

        msg = """
                Hi %s,

                This email is to inform you that the book(s) you borrowed
                (%s) is due or about to be due. Please endeveour to return it on time.

                Best Regards
                Andela Librarian
                """ %(name, book)
        if name and book:
            send_mail('Due book(s) notification', msg, 'andela.library@andela.co', 
                    [names])

    return HttpResponseRedirect('/book-status/')



    