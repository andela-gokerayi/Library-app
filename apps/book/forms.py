from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, Textarea, DateInput, HiddenInput
from django.forms import ModelChoiceField
from apps.book.models import Book, BookLease
from apps.libraryuser.models import Fellow

# TODO: verify quantity greater than zero
class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'quantity', 'source', 'isbn_number']
        widgets = {
            'category': Select(attrs={'id': 'id_category'})
        }

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'quantity', 'source', 'isbn_number']
        widgets = {
            'date_recieved': DateInput(attrs={'type': 'date', 'class': 'datepicker'}, format='%Y-%m-%d'),
        }


class LendBookForm(ModelForm):

    class Meta:
        model = BookLease
        fields = ['book', 'borrower', 'due_date']
        widgets = {
            'book': HiddenInput(),
            'borrower': Select(attrs={'id': 'borrower', 'class': 'browser-default chosen-select'}),
            'due_date': DateInput(attrs={'type': 'date', 'class': 'datepicker',
                'id': 'due_date'}, format='%Y-%m-%d'),
        }

