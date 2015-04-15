import datetime
from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, Textarea
from apps.book.models import Book, BookLease


class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'quantity', 'source', 'isbn_number', 'date_recieved']

class LendBookForm(forms.ModelForm):
    class Meta:
        model = BookLease
        fields = ['book', 'borrower', 'borrowed_date', 'return_date', 'due_date']

        widgets = {
            'book': Select(attrs={}),
            'borrower': Select(attrs={})
        }
