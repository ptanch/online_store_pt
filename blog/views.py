from blog.models import Blog
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "creation_date", "is_published", "views_number")
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        """Переопределение метода, чтобы увеличить счётчик просмотров"""
        obj = super().get_object(queryset)
        obj.views_number += 1
        obj.save(update_fields=['views_number'])
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "creation_date", "is_published", "views_number")
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
