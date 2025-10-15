from blog.models import Blog
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "creation_date", "is_published", "views_number")
    success_url = reverse_lazy('blog:blog_list')
