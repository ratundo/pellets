from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models

from content.models import Blog, Faq


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget()},
    }


admin.site.register(Faq)
admin.site.register(Blog, BlogAdmin)
