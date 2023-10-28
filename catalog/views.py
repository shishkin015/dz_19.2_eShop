from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category


# Create your views here.


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Категории'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()
        return context_data


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product_category_id=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Каталог {category_item.сategory_name}'

        return context_data


class ProductCreateView(CreateView):
    model = Product
    extra_context = {
        'title': 'Добавить продукт'
    }
    fields = ('product_name', 'product_description', 'product_preview', 'product_category', 'product_price',)
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    extra_context = {
        'title': 'Изменить продукт'
    }
    fields = ('product_name', 'product_description', 'product_preview', 'product_category', 'product_price',)

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.product_category.pk])


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {
        'title': 'Удалить продукт'
    }

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.product_category.pk])


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}\n{phone}\n{message}')

    context = {'title': 'Контакт'}
    return render(request, 'catalog/contacts.html', context)
