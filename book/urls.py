from django.conf.urls import patterns, url
from book import views
from book.views import BookListView


urlpatterns = patterns('',
    url(r'^$', views.index, name='book-index'),
    url(r'^add-book/$', views.get_book, name='add-book'),
    url(r'^books/$', BookListView.as_view(), name='books-list'),
)