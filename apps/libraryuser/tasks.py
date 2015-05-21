from __future__ import absolute_import

from celery import shared_task
from apps.book.models import BookLease
from django.core.mail import send_mail
from django.utils import timezone

@shared_task
def send_admin_mail(*args, **kwargs):
    borrowed_books = BookLease.objects.all()

    for book in borrowed_books:
        check_month = timezone.now().month == book.due_date.month
        check_almost_due = abs(book.due_date.day - timezone.now().day)
        print book.borrower.email
        if check_month and check_almost_due <= 2:
            send_mail("Book due", "It is about to be due", "andela.library@andela.co",
               [book.borrower.email], fail_silently=False) 
        else:
            None  


    