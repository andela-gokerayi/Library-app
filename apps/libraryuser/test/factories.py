import factory

from django.contrib.auth.models import User
from apps.libraryuser.models import Fellow

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = u'eniola'
    email = u'eniola@example.com'


class FellowFactory(factory.DjangoModelFactory):
    class Meta:
        model = Fellow

    first_name = u'John'
    email = u'john@example.com'