from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import formset_factory, inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Категории'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset().filter(product_category_id=self.kwargs.get('pk'))

        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Каталог {category_item.сategory_name}'

        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    extra_context = {
        'title': 'Добавить продукт'
    }
    # fields = ('product_name', 'product_description', 'product_preview', 'product_category', 'product_price',)
    form_class = ProductForm
    permission_required = 'catalog.add_catalog'
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    extra_context = {
        'title': 'Изменить продукт'
    }
    # fields = ('product_name', 'product_description', 'product_preview', 'product_category', 'product_price',)
    form_class = ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.product_category.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    extra_context = {
        'title': 'Удалить продукт'
    }

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.product_category.pk])


@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}\n{phone}\n{message}')

    context = {'title': 'Контакт'}
    return render(request, 'catalog/contacts.html', context)
