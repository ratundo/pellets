from django.contrib import admin

from goods.models import Factory, Goods

# Register your models here.
admin.site.register([Goods, Factory])
