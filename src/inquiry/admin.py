from django.contrib import admin

from inquiry.models import Customer, Inquiry

# Register your models here.
admin.site.register([Customer, Inquiry])
