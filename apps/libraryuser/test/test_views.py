from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from django.contrib.auth.models import User
from apps.libraryuser import views
from apps.libraryuser.models import *


class LibraryUserTests(TestCase):

    def setUp(self):
        self.password = 'secret'
        self.user = User.objects.create_superuser(username='admin', password=self.password, email='admin@admin.com')

    def test_index(self):
        response = self.client.get('/')
        self.assertContains(response, 'A library is the delivery room for the birth of ideas, ' 
            '<br>a place,<br> where history comes to life.')

    def test_get_login_request(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Login as Admin')

    def test_log_in_log_out(self):
        response = self.client.post(
            reverse('login'), {'username': self.user.username, 'password': self.password})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['_auth_user_id'], self.user.id)

        self.client.get(reverse('logout'))

        self.assertFalse('_auth_user_id' in self.client.session)

    def test_login_fails_with_an_invalid_id(self):
        response = self.client.post(
            reverse('login'), {'username': self.user.username, 'password': 'jess'})

        self.assertFalse('_auth_user_id' in self.client.session)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Login as Admin')

