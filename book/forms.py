from django import forms

class AddForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    author = forms.CharField(label='author', max_length=100)
    category = forms.CharField(label='category', max_length=100)
    quantity = forms.IntegerField(required=True)
    available = forms.IntegerField(required=True)
    borrowed = forms.IntegerField(required=True)