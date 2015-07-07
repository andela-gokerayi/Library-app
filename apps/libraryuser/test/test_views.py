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
        self.assertEqual(response.status_code, 200)

    def test_log_in_log_out(self):
    
        client = Client()

        response = client.post(
            reverse('login'), {'username': self.user.username, 'password': self.password})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(client.session['_auth_user_id'], self.user.id)

        client.get(reverse('logout'))

        self.assertFalse('_auth_user_id' in client.session)
