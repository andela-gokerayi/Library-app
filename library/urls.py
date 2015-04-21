from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from apps.book.views import BookListView
from apps.book.views import BookDetailView
# from apps.book.views import BorrowBookView
from apps.book.views import get_book
from apps.book.views import borrow_book
from apps.libraryuser.views import BookIndexListView, auth_view, login, logout
from apps.libraryuser.views import HomeView
from apps.libraryuser.models import Fellow

urlpatterns = patterns ('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^detail/(?P<pk>[-_\w]+)', BookDetailView.as_view(), name='book-detail'),
    url(r'^home/', BookIndexListView.as_view(), name='book-index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth-user/$', auth_view, name='auth-user'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^book-status/$', BookListView.as_view(), name='book-list'),
    url(r'^add-book/$', login_required(get_book), name='add-book'),
    url(r'^edit-book/(?P<id>\d+)/$', login_required(get_book), name='edit-book'),
    url(r'^borrow/(?P<id>\d+)/$', borrow_book, name='borrow-book'),
    # url(r'^accounts/register/$', register_user),
)

   