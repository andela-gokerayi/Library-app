from django.db import models
from django.contrib.auth.models import User as DjangoUser


DjangoUser._meta.get_field('first_name').max_length=50
DjangoUser._meta.get_field('last_name').max_length=50
DjangoUser._meta.get_field('email').max_length=100
DjangoUser._meta.get_field('username').max_length=100
DjangoUser._meta.get_field('is_staff').default=True
DjangoUser._meta.get_field('is_superuser').default=True


class StaffUser(models.Model):
    user = models.OneToOneField(DjangoUser)

    def __unicode__(self):
        return '{}'.format(self.user.username)


class Fellow(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' %(self.first_name, self.last_name)
