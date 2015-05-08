from django.db import models
import datetime

from apps.libraryuser.models import StaffUser, Fellow


class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField(max_length=100, unique=True)
    date_recieved = models.DateField(default=datetime.datetime.now())
    quantity = models.PositiveIntegerField(default=0, null=True)
    source = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def get_num_available_book(self):
        total_leased = self.book_leases.all().count()
        available = self.quantity - total_leased
        return available
    
    num_book_available = property(get_num_available_book)
        
    def __unicode__(self): 
        return '{}'.format(self.title)


class BookLease(models.Model):
    book = models.ForeignKey(Book, related_name='book_leases')
    borrower = models.ForeignKey(Fellow)
    borrowed_date = models.DateField(default=datetime.datetime.now())
    return_date = models.DateField(default=datetime.datetime.now())
    due_date = models.DateField(default=datetime.datetime.now())
    returned = models.NullBooleanField()

    def __unicode__(self): 
        return '{}'.format(self.book)
