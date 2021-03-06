from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from apps.book.models import Book, BookLease, BookBorrowRequest

# Register your models here.
AdminSite.site_header = "Andela Library"

admin.site.register(Book)
admin.site.register(BookLease)
admin.site.register(BookBorrowRequest)