from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView
from pytils.translit import slugify

from blog.models import Blog


class IndexView(TemplateView):
    template_name = 'blog/index.html'
    extra_context = {
        'title': 'Статьи'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Blog.objects.all()
        return context_data


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview')
    extra_context = {
        'title': 'Добавить статью'
    }
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview',)
    extra_context = {
        'title': 'Редактировать статью'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('slug')])


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Список активных статей'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog
    # template_name = 'blog/blog_detail.html'
    # slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        blog_item = Blog.objects.get(slug=self.kwargs.get('slug'))
        context_data['blog_pk'] = blog_item.pk,
        context_data['title'] = f'{blog_item.title}'

        return context_data


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Удалить статью'
    }


def toggle_activity(request, slug):
    blog_item = get_object_or_404(Blog, slug=slug)
    blog_item.is_published = False if blog_item.is_published else True

    blog_item.save()

    return redirect(reverse('blog:index'))
