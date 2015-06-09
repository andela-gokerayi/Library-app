from django.contrib import admin
from apps.libraryuser.models import StaffUser, Fellow

# Register your models here.
admin.site.register(StaffUser)
admin.site.register(Fellow)