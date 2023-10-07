from django.shortcuts import render  # NOQA
from django.views.generic import DetailView, ListView

from content.models import Blog, Faq


# Create your views here.
class FaqView(ListView):
    model = Faq
    template_name = "faq.html"
    context_object_name = "faq"


class BlogListView(ListView):
    model = Blog
    template_name = "blog-list.html"
    context_object_name = "blog"


class BlogPostView(DetailView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blog_post"
