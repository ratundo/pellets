from django.db import models
from django.utils.text import slugify


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question


class Blog(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    text = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
