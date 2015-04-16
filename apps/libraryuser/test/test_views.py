from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from apps.libraryuser import views
from apps.libraryuser.models import *


class LibraryUserTests(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_log_in(self):

        client = Client()

        response = client.post(
            reverse('login'), {'username': 'ife', 'password': 'password'})
        user = Fellow.objects.get(id='0')
        self.assertEqual(client.session['_auth_user_id'], user.id)


    def test_log_out(self):

        client = Client()

        client.post(
            reverse('login'), {'username': 'ife', 'password': 'password'})
        user = Fellow.objects.get(id='0')

        client.get(reverse('logout'))
        self.assertNotIn('_auth_user_id', client.session)