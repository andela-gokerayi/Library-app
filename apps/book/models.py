from django.db import models
# from django.db.models.manager import Manager
from apps.libraryuser.models import StaffUser, Fellow


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
    borrowed_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    returned = models.NullBooleanField()

    # def get_num_available_book(self):

        # book = Book.objects.get(id=id)
    #     total_leased = self.book_leases.all().count()
    #     available = self.quantity - total_leased
    #     return available
    
    # num_book_available = property(get_num_available_book)

    def __unicode__(self): 
        return '{}'.format(self.book)

    # def get_num_available_book(self, filter=None):
    #     available = 0



    # def get_num_available(self, filter=None):
    #     available = 0
    #     obj = self.booklease.all()
    #     if filter==None:
    #         for book in obj:
    #             num_available = 
    #          def get_amount_paid(self, filter=None):
    #     amount_paid = 0
    #     obj = self.payment_histories.all()
    #     if filter==None:
    #         if obj:
    #             for item in obj:
    #                 amount_paid = amount_paid + item.sum_paid
    #                 continue
    #         else:
    #             amount_paid = '--'
    #     else:
    #         try:
    #             current_obj = self.payment_histories.filter(date=filter)
    #             current_obj_id = current_obj[0].id
    #             for item in obj:
    #                 if item.id < current_obj_id:
    #                     amount_paid = amount_paid + item.sum_paid
    #                 continue
    #         except Exception, e:
    #             amount_paid = '--'
            
    #     return amount_paid

    # objects = BookManager()

    # def get_num_borrower(self):
    #     borrower = self.borrower.all().count()
    #     return borrower

    # def get_num_available(self):
    #     available = 0
    #     for borrower in borrowers:
    #         if returned == True:
    #             available = Book.objects.count() + available
    #         else:
    #             available = available - Book.objects.count()
    #     return available

