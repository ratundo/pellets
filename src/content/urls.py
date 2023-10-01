from django.urls import path

from content.views import BlogListView, BlogPostView, FaqView

app_name = "content"  # NOQA

urlpatterns = [
    path("faq/", FaqView.as_view(), name="faq"),
    path("blog/", BlogListView.as_view(), name="blog"),
    path("blog/<slug:slug>", BlogPostView.as_view(), name="blog_post"),
]
