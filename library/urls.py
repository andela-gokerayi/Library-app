from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

from apps.book.views import BookListView, BookLeaseListView
from apps.book.views import BookLeaseDetailView, BookDetailView 
from apps.book.views import book_delete
from apps.book.views import get_book
from apps.book.views import edit_book
from apps.book.views import borrow_book
from apps.libraryuser.views import  auth_view, login, logout
from apps.libraryuser.views import HomeView
from apps.libraryuser.models import Fellow
from apps.libraryuser.tasks import send_admin_mail

urlpatterns = patterns ('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^detail/(?P<pk>[-_\w]+)', login_required(BookDetailView.as_view()), name='book-detail'),
    url(r'^book-detail/(?P<pk>[-_\w]+)', login_required(BookLeaseDetailView.as_view()), name='booklease-detail'),
    url(r'^home/$', login_required(BookListView.as_view()), name='book-list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth-user/$', auth_view, name='auth-user'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^book-status/$', login_required(BookLeaseListView.as_view()), name='booklease-list'),
    url(r'^add-book/$', get_book, name='add-book'),
    url(r'^edit-book/(?P<id>\d+)/$', edit_book, name='edit-book'),
    url(r'^borrow/(?P<id>\d+)/$', borrow_book, name='borrow-book'),
    url(r'^delete/(?P<pk>\d+)$', book_delete, name='book_delete'),
    url(r'^send-mail/$', send_admin_mail, name='send_mail'),
)
   