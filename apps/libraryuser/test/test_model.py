from django.test import TestCase
from django.db import models
from apps.libraryuser.models import Fellow, StaffUser
from django.contrib.auth.models import User as DjangoUser
import logging as logger


class FellowModelTest(TestCase):

    def test_model_fields(self):

        fields = {field.name: field for field in Fellow._meta.fields}
        self.assertTrue('first_name' in fields)
        self.assertTrue('last_name' in fields)
        self.assertTrue('email' in fields)

    def test_string_representation(self):
        user = Fellow(first_name='John', \
                    last_name='Ladna', email='be@gmail.com')
        logger.info(user)
        assert "John Ladna" in str(user)


class StaffUserModelTest(TestCase):

    def test_model_field(self):

        fields = {field.name: field for field in StaffUser._meta.fields}

        self.assertTrue('user' in fields)
