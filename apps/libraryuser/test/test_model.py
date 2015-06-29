import factory
from django.test import TestCase
from django.db import models
from apps.libraryuser.models import Fellow, StaffUser
from django.contrib.auth.models import User as DjangoUser

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = DjangoUser

    username = 'eniola'

class FellowFactory(factory.DjangoModelFactory):
    class Meta:
        model = Fellow

    first_name = u'Eniola'
    last_name = u'Arinde'

class StaffUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = StaffUser

    user = factory.SubFactory(UserFactory)


class FellowModelTest(TestCase):

    def test_model_fields(self):

        fields = {field.name: field for field in Fellow._meta.fields}
        self.assertTrue('first_name' in fields)
        self.assertTrue('last_name' in fields)
        self.assertTrue('email' in fields)

    def test_string_representation(self):
        user = Fellow(first_name='John', \
                    last_name='Ladna', email='be@gmail.com')
        assert "John Ladna" in str(user)

    def test_unicode_method_when_there_is_no_fellow(self):
        fellow = Fellow()

        name = fellow.__unicode__()

        self.assertEqual(' ', name)

    def test_unicode_method_when_there_is_a_fellow(self):
        fellow = FellowFactory()

        name = fellow.__unicode__()

        self.assertEqual('Eniola Arinde', name)

class StaffUserModelTest(TestCase):

    def test_model_field(self):

        fields = {field.name: field for field in StaffUser._meta.fields}

        self.assertTrue('user' in fields)

    def test_unicode_method(self):
        staff = StaffUserFactory()

        username = staff.__unicode__()

        self.assertEqual('eniola', username)
