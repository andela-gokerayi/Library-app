from django.db import models
# from django.db.models.manager import Manager
from apps.libraryuser.models import StaffUser, Fellow
import datetime



class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField(max_length=100, unique=True)
    date_recieved = models.DateField()
    quantity = models.PositiveIntegerField(default=0, null=True)
    source = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def get_num_available_book(self):

        # book = Book.objects.get(id=id)
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
    return_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    returned = models.NullBooleanField()


    def __unicode__(self): 
        return '{}'.format(self.book)

 
