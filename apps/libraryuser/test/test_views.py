from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from django.contrib.auth.models import User
from apps.libraryuser import views
from apps.libraryuser.models import *


class LibraryUserTests(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_log_in(self):
        password = 'secret'
        user = User.objects.create_superuser(username='admin', password=password, email='admin@admin.com')
    
        client = Client()

        response = client.post(
            reverse('login'), {'username': user.username, 'password': password})
        
        self.assertEqual(True, user.is_authenticated())
        self.assertEqual(client.session['_auth_user_id'], user.id)


    def test_log_out(self):

        client = Client()

        client.post(
            reverse('login'), {'username': 'ife', 'password': 'password'})
        user = Fellow.objects.get(id='0')

        client.get(reverse('logout'))
        self.assertNotIn('_auth_user_id', client.session)