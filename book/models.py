from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=100, unique=True)
    isbn_number = models.CharField(max_length=100, unique=True)
    date_recieved = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0, null=True)
    source = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, unique=True)

    def __unicode__(self): 
        return '{}'.format(self.title)

class BookStatus(models.Model):
    title = models.ForeignKey(Book, related_name='title_status')
    quantity = models.PositiveIntegerField(default=0, null=True)
    available = models.PositiveIntegerField(default=0, null=True)
    borrowed = models.PositiveIntegerField(default=0, null=True)
    author = models.OneToOneField(Book, to_field='author', related_name='author_status', unique=True)
    category = models.OneToOneField(Book, to_field='category', related_name='category_status', unique=True)

class LendBook(models.Model):
    title = models.ForeignKey(Book, related_name='title_lend')
    borrower = models.CharField(max_length=250)
    borrower_email = models.EmailField(max_length=254)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    due_date = models.DateField()
    author = models.OneToOneField(Book, to_field='author', related_name='author_lend', unique=True)
    isbn_number = models.OneToOneField(Book, to_field='isbn_number', related_name='isbn_number_lend', unique=True)