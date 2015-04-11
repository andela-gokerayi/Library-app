from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from book.models import Book, BookStatus,LendBook

# Register your models here.
AdminSite.site_header = "Andela Library"

admin.site.register(Book)
admin.site.register(BookStatus)
admin.site.register(LendBook)
# admin.site.register(LendBook)