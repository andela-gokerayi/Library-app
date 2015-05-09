import datetime
from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, Textarea, DateInput
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
        widgets = {
            'date_recieved': DateInput(attrs={'type': 'date', 'class': 'datepicker'}, format='%Y-%m-%d'),
        }


class LendBookForm(ModelForm):

    class Meta:
        model = BookLease
        fields = ['book', 'borrower', 'borrowed_date', 'due_date'] 
        widgets = {
            'borrowed_date': DateInput(attrs={'type': 'date', 'class': 'datepicker'}, format='%Y-%m-%d'),
            'due_date': DateInput(attrs={'type': 'date', 'class': 'datepicker'}, format='%Y-%m-%d'),
        }

