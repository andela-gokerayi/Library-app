from django.contrib import admin
from apps.libraryuser.models import StaffUser, Fellow
from kombu.transport.django import models as kombu_models


# Register your models here.
admin.site.register(StaffUser)
admin.site.register(Fellow)
admin.site.register(kombu_models.Message)