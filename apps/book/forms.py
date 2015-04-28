import datetime
from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, Textarea
from django.forms import ModelChoiceField
from apps.book.models import Book, BookLease
from apps.libraryuser.models import Fellow


class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'quantity', 'source', 'isbn_number', 'date_recieved']

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'quantity', 'source', 'isbn_number', 'date_recieved']

class LendBookForm(ModelForm):

    class Meta:
        model = BookLease
        fields = ['book', 'borrower'] 

