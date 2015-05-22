
from django.db import models
from datetime import datetime, date
from datetime import timedelta
import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone
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


def get_deadline():
    return datetime.datetime.now() + timedelta(days=14)

class BookLease(models.Model):
    book = models.ForeignKey(Book, related_name='book_leases')
    borrower = models.ForeignKey(Fellow)
    borrowed_date = models.DateField(default=datetime.datetime.now())
    return_date = models.DateField(default=datetime.datetime.now())
    due_date = models.DateField(default=get_deadline)
    returned = models.NullBooleanField()

    def book_is_due(self):
        check_month = timezone.now().month == self.due_date.month
        now = date(timezone.now().year, timezone.now().month, timezone.now().day)
        then =  date(self.due_date.year, self.due_date.month, self.due_date.day)
        check_day = abs((now - then).days)

        if check_month and check_day == 0:
            return "due"
        elif check_month and check_day <= 2:
            return "about"

    def __unicode__(self): 
        return '{}'.format(self.book)
